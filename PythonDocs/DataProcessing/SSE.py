import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy


# THIS IS THE ENGLISH MST CORPUS 
stopwords = nltk.corpus.stopwords.words('english')
f=open('/Users/chadgevans/Desktop/PythonDocs/DataProcessing/CorpusEnglish.txt','r')
lines=f.readlines()

MSTText=[]
for line in lines:
	line = line.rstrip()
	MSTText.extend(nltk.word_tokenize(line))
	
res = []
for w in MSTText:
	if w not in stopwords:
		res.append(w)
	
text=res

#Basic Word Statistics
len(text) # number of tokens (79,964 on 3/15)
clean_text=([w.lower() for w in text if w.isalpha()])
len(clean_text) #(49,798 on 3/15)

len(set(text)) # number of word types (15,910 on 3/15)
#sorted(set(text)) # sorted vocabulary, good place to check words of interest
clean_text_set=set([w.lower() for w in text if w.isalpha()]) # cleaned so only alpha and lower
len(clean_text_set) # 9,912 on 3/15



