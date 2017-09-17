import nltk
import pylab
import re
import os
import sys
from CA import *


f=open('/Users/chadgevans/Desktop/PythonDocs/DataProcessing/Corpus.txt','r')
lines=f.readlines()

nltk.word_tokenize(lines[0])

MST_tokens = []
for line in lines:
line = line.rstrip() 
MST_tokens.extend(nltk.word_tokenize(line))
# MST_tokens

