import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy
import chunk
from nltk. chunk import tag_pattern2re_pattern
from nltk. chunk import RegexpParser
from nltk import bigrams
from nltk.probability import FreqDist
from nltk import trigrams

# THIS IS Just Ten ENGLISH MST Articles 

stopwords = nltk.corpus.stopwords.words('english')
f=open('/Users/chadgevans/Desktop/Justten.txt','r')
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
clean_text=([w.lower() for w in text if w.isalpha()])
corpus10=clean_text

tagged=nltk.pos_tag(corpus10)

#######################

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result
result.draw()

nltk.app.chunkparser() # interesting application

grammar = r"""
NP: {<DT|PP\$>?<JJ>*<NN>}
{<NNP>+}
"""
cp = nltk.RegexpParser(grammar)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
print cp.parse(sentence)

