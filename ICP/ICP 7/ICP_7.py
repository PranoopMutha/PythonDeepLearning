from bs4.element import Comment
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.stem import PorterStemmer,LancasterStemmer,SnowballStemmer, WordNetLemmatizer
from nltk import wordpunct_tokenize,pos_tag,ne_chunk
from nltk.util import ngrams

# url = urllib.request.urlopen("https://en.wikipedia.org/wiki/Google").read().decode('utf-8')
# soup = BeautifulSoup(url, 'html.parser')
# texts = soup.find_all(text=True)
#
# def tag_visible(element):
#     if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
#         return False
#     if isinstance(element, Comment):
#         return False
#     return True
#
# result = filter(tag_visible, texts)
# f = open('input1.txt','w')
# f.writelines(result)

f1 = open("input1.txt", "r")
fileread = f1.read()


senttokens = nltk.sent_tokenize(fileread)
wordtokens = nltk.word_tokenize(fileread)
print("*****************Sentence Tokenizer*******************")
for s in senttokens:
    print(s)
print("*****************Word Tokenizer*******************")
for w in wordtokens:
    print(w)

print("*****************POS Tagging*******************")
print(nltk.pos_tag(wordtokens))

print("*****************Stemming*******************")
ps = []
ls = []
ss = []
print("*****************Porter Stemming*******************")
pStemmer = PorterStemmer()
for w in wordtokens:
    ps.append(pStemmer.stem(w))
print(ps)
print("*****************Lancaster Stemming*******************")
lStemmer = LancasterStemmer()
for w in wordtokens:
    ls.append(lStemmer.stem(w))
print(ls)
print("*****************Snowball Stemming*******************")
sStemmer = SnowballStemmer('english')
for w in wordtokens:
    ss.append(sStemmer.stem(w))
print(ss)

print("*****************Lemmatization*******************")

ltzr = []
lemmatizer = WordNetLemmatizer()
for w in wordtokens:
    ltzr.append(lemmatizer.lemmatize(w))
print(ltzr)

print("*****************Named Entity Recognition*******************")

ner = []
for s in senttokens:
    ner.append(ne_chunk(pos_tag(wordpunct_tokenize(s))))
print(ner)

print("*****************Trigram*******************")

tg = ngrams(wordtokens,3)
for t in tg:
    print(t)


