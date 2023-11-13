#                           Assignment No.: 3
# Write a program for Pre-processing of a Text Document: stop word removal.

import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))
file1 = open("IR\sample1.txt")


line = file1.read()
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('IR/filteredtext.txt', 'a')
        appendFile.write(" "+r)
        appendFile.close()
