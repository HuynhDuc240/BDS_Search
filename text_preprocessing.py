import re
from underthesea import word_tokenize
from collections import Counter

class Preprocessing():
    def __init__(self, path_stop_word):
        stopwords_file = open(path_stop_word, encoding = 'utf8')
        self.stopwords = list(map(lambda x: x.replace('\n', ''), stopwords_file))

    def get_terms(self, content):
        content = content.replace('<br/>', ' ')
        content = content.lower()
        #content = re.sub(r'[.,")(]', '', content)
        content = re.sub(r'[^\w\s]', ' ', content)
        content = re.sub(r'\s+', ' ', content).strip() # strip loại bỏ khoảng trắng đầu cuối
        tokens = word_tokenize(content)
        terms = []
        for term in tokens:
            if term not in self.stopwords:
                terms.append(term)
        return Counter(terms)
