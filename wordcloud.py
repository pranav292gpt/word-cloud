import re 
from collections import Counter

#Input text as words
def words(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('98-0.txt').read()))

stopwords = words(open('stopwords').read())

def word_cloud():
    most_common = []
    i=0
    for object in WORDS.most_common():
        if object[0] not in stopwords:
            most_common.append(object[0])
    return most_common[:10]
