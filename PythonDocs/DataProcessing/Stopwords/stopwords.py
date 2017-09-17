import nltk
import pylab
import re
import os
import sys
from CA import *

f=open('/Users/chadgevans/Desktop/PythonDocs/MSTCorpus/4.txt','r')
lines=f.readlines()
stopwords=open('/Users/chadgevans/Desktop/PythonDocs/Stopwords/portuguese.txt','r')

mytokens = []
for line in lines:
line = line.rstrip() 
mytokens.extend(nltk.word_tokenize(line))

# stop words for loop
for x in mytokens:
	if x in stopwords:
		delete x from mytokens
		
# SyntaxError: invalid syntax (indicates the x in the last line)
# As of 9:30 March 14, stopwords not working