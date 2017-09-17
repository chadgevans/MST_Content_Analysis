import nltk
import lxml.html
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

print mytokens[:100]
print mytokens[250:300]


# Attempts at cleaning
#t=lxml.html.fromstring("...")
#t.text_content()
#''.join(BeautifulSoup(value, convertEntities=BeautifulSoup.HTML_ENTITIES).findAll(text=True))