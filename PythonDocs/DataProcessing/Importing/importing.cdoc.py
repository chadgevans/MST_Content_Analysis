import nltk
import pylab
import re
import os
import sys
from CA import *


f=open('/Users/chadgevans/Desktop/PythonDocs/MSTEnglish/C.txt','r')
lines=f.readlines()

nltk.word_tokenize(lines[0])

mytokens = []
for line in lines:
line = line.rstrip() 
mytokens.extend(nltk.word_tokenize(line))
 #mytokens