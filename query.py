from text_preprocessing import *
from SQLiteHelper import *
from ast import literal_eval
import math
import numpy as np

inverted_index = SQLiteHelper('resource/inverted_index.db')
data = SQLiteHelper('resource/data.db')
total_number_doc = inverted_index.get_len()
text_prep = Preprocessing('vietnamese-stopwords.txt')


def cosin(vq, vd):
    mult_vq_vd = sum(vq*vd)
    sqrt_sum_square_vq = math.sqrt(sum(np.square(vq)))
    sqrt_sum_square_vd = math.sqrt(sum(np.square(vd)))
    if sqrt_sum_square_vd == 0:
        return 0
    return round(mult_vq_vd/(sqrt_sum_square_vd*sqrt_sum_square_vq), 4)

def normalize_vector_docs(terms_rows):
    num_term = len(terms_rows)
    row = 0
    term_root = terms_rows[0][0]
    posting_list_root = literal_eval(terms_rows[0][2])
    for term, df, posting_list in terms_rows:
        if row != 0:
            posting_list = literal_eval(posting_list)
        else:
            posting_list = posting_list_root
        for doc, tf in posting_list.items():
            idf = 1 + math.log(total_number_doc/float(df))
            weight = tf*idf
            if term != term_root:
                if doc in posting_list_root:
                    posting_list_root[doc][row] = weight
                else:
                    posting_list_root[doc] = np.zeros(num_term)
                    posting_list_root[doc][row] = weight
            else:
                posting_list_root[doc] = np.zeros(num_term)
                posting_list_root[doc][row] = weight
        row+=1
    return posting_list_root

def cosin_from_query_to_docs(vector_query, terms_rows):
    vector_docs = normalize_vector_docs(terms_rows)
    list_cosin = [[cosin(vector_query, vector_doc), doc] for doc, vector_doc in vector_docs.items()]
    list_cosin = sorted(list_cosin, key = lambda x: x[0], reverse = True)
    return list_cosin

def tf_idf_query(terms_query, terms_rows):
    tf_query = np.array(list(map(lambda x: 1 + math.log(x[1]), terms_query)))
    idf_query = np.array([1 + math.log(total_number_doc/t[1]) for t in terms_rows])
    return tf_query*idf_query

def remove_term_not_in_db(terms_query, terms_rows):
    for index, row in enumerate(terms_rows):
        if row == -1:
            del terms_query[index]
            del terms_rows[index]

def Query(query):
    terms_query = text_prep.get_terms(query)
    terms_query = [[key, value] for key, value in terms_query.items()]
    terms_rows = [inverted_index.get_row_by_term(t[0]) for t in terms_query]
    remove_term_not_in_db(terms_query, terms_rows)
    if len(terms_query) == 0:
        return ''
    vector_query = tf_idf_query(terms_query, terms_rows)
    result = cosin_from_query_to_docs(vector_query, terms_rows)[:100]
    return result

def export_to_csv(result):
    with open('result.csv', 'w', encoding = 'utf8') as file:
        file.write('link\ttitle\tlocation\timage\tarea\tprice\n')
        for _, doc in result:
            info = data.select('SELECT * FROM data where rowid = %d'%(doc+1))[0]
            file.write('%s\t%s\t%s\t%s\t%s\t%s\n'%(info[0], info[1], info[2], info[3], info[4], info[5]))
# def main():
#     result = Query()
#     export_to_csv(result)

# if __name__ == "__main__":
#     main()