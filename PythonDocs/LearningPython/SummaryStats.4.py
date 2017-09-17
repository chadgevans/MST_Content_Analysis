import nltk
import pylab
import re
import os
import sys
from CA import *


f=open('/Users/chadgevans/Desktop/PythonDocs/MSTCorpus/4.txt','r')
lines=f.readlines()

nltk.word_tokenize(lines[0])

mytokens = []
for line in lines:
line = line.rstrip() 
mytokens.extend(nltk.word_tokenize(line))
text=mytokens

#1
len(text) # number of tokens
len(set(text)) # number of word types
sorted(set(text)) # sorted vocabulary
set([w.lower() for w in text if w.isalpha()]) # vocab, lower, ignore punctuation

# for word in text:   (general for loop) PLUS INDENT
# if len (word) < 5: (general for condition) PLUS INDENT
FIND FREQUENCY DISTRIBUTION (words of text nad frequency)

#2 & 3
#use import to call programs
# help(v) to find out about v
#iterate over file with for line in open(f)
# re.findall() # to find all substrings in a string that mathc a pattern

#4
# ofile=open('output.txt','w'
#then adding content to the file ofile.write("Monty Python"), 
#and finally closing the file ofile.close().
