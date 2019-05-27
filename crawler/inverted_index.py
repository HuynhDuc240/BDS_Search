import re
from termcolor import colored
import pandas as pd
from underthesea import word_tokenize
import json
import pandas as pd
import glob

path = r'C:\Users\Huynh Duc\Desktop\Bat_dong_san' # use your path
all_files = glob.glob(path + "/*_detail.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, sep="\t")
    li.append(df)
detail = pd.concat(li, axis=0, ignore_index=True)
# print(detail)
all_files = glob.glob(path + "/*_info.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, sep="\t")
    li.append(df)
title = pd.concat(li, axis=0, ignore_index=True)
# print(title)
class Appearance:
    def __init__(self, docID, frequency):
        self.docID = docID
        self.frequency = frequency
    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)
    def add(self, a_docID, a_frequency):
        self.docID = self.docID + "," + a_docID
        self.frequency = str(self.frequency) + "," + str(a_frequency)
class Database:
    """
    In memory database representing the already indexed documents.
    """
    def __init__(self):
        self.db = dict()

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.__dict__)
    
    def get(self, id):
        return self.db.get(id, None)
    
    def add(self, document):
        """
        Adds a document to the DB.
        """
        return self.db.update({document['id']: document})

    def remove(self, document):
        """
        Removes document from DB.
        """
        return self.db.pop(document['id'], None)

class InvertedIndex:
    """
    Inverted Index class.
    """
    def __init__(self,db):
        self.index = dict()
        self.db = db

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)
        
    def index_document(self, document):
        """
        Process a given document, save it to the DB and update the index.
        """
        
        # Remove punctuation from the text.
        clean_text = re.sub(r'[\n,*().\-\:]',' ', document['text'])
        
        terms = word_tokenize(clean_text.lower())
        appearances_dict = dict()
        # Dictionary with each term and the frequency it appears in the text.
        for term in terms:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)
            
        # Update the inverted index
        update_dict = { key: [appearance]
                       if key not in self.index
                       else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items() }
        self.index.update(update_dict)
        # Add the document into the database
        self.db.add(document)
        return document
    
    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances. 
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return { term: self.index[term] for term in query.split('/r') if term in self.index }

def highlight_term(id, term, text):
    replaced_text = text.replace(term, colored(term, 'red', attrs=['reverse', 'blink']))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)

def merge(root, branch):
    print(len(root.index))
    if len(root.index) == 0:
        root.index = branch.index
        root.db = branch.db
    else:
        for word in branch.index.keys():
            finder = root.index.get(word)
            if finder != None:
                if root.index[word][0].docID == branch.index[word][0].docID and root.index[word][0].frequency == branch.index[word][0].frequency:
                    continue
                root.index[word][0].docID = root.index[word][0].docID + ","+ branch.index[word][0].docID
                root.index[word][0].frequency = str(root.index[word][0].frequency) + "," +str(branch.index[word][0].frequency)
                # print(finder)
            else:
                root.index.update(branch.index)
                # print(branch.index[word])
   
if __name__ == "__main__":
    db = Database()
    index = InvertedIndex(db)
    root = InvertedIndex(db)
    # detail = pd.read_csv("cho-thue-can-ho-chung-cu_detail.csv",sep="\t")
    # title = pd.read_csv("cho-thue-can-ho-chung-cu.csv",sep="\t")
    
    for i in range(len(detail)):
        data = Database()
        branch = InvertedIndex(data)
        d = detail["detail"][i].replace("<br/>","\n")
        t = title["title"][i]
        text = t + "\n" + d
        document = {
            'id': str(i),
            'text': text
        }
        branch.index_document(document)
        merge(root,branch)
    with open('inverted_index.json', 'w', encoding='utf8') as f:
        json.dump(str(root.index), f, ensure_ascii=False)
    # print(root.index)
    # for i in index.index.keys():
    #     print(i)
    # text = "ban công"
    # search_term = input("Enter term(s) to search: ")
    # result = index.lookup_query(search_term)
    # if len(result) == 0:
    #     print("NOT FOUND")
    # else:
    #     for term in result.keys():
    #         for appearance in result[term]:
    #             # print(type(appearance))
    #             # Belgium: { docId: 1, frequency: 1}
    #             document = db.get(appearance.docID)
    #             print(highlight_term(appearance.docID, term, document['text']))
    #         print("-----------------------------")    
        
