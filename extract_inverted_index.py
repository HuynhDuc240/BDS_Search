from SQLiteHelper import *
import pandas as pd
import glob
from text_preprocessing import *
import math

inverted_index_db = SQLiteHelper('inverted_index.db')
inverted_index_dict = {}
text_prep = Preprocessing('vietnamese-stopwords.txt')

def addToDict(dictionary, term, f, doc):
    if term not in dictionary:
        dictionary[term] = [1, {doc: f}]
    else:
        dictionary[term][0]+=1
        dictionary[term][1][doc] = f

def inverted_index():
    global inverted_index_dict
    doc_files = pd.read_csv('resource/data_detail.csv', sep = ' ')
    documents = doc_files.detail
    for index, doc in enumerate(documents):
        terms = text_prep.get_terms(doc)
        for t, f in terms.items():
            tf = 1 + math.log(f)
            addToDict(inverted_index_dict, t, tf, index)

def convert_to_database():
    for key, value in inverted_index_dict.items():
        inverted_index_db.insert(key, value[0], str(value[1]))

def main():
    inverted_index()
    convert_to_database()

if __name__ == "__main__":
    main()