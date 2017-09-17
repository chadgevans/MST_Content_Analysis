import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy

stopwords=['o','a']

text="o menino fica a frente da janela.  A menina não o gosta que fique assim."
text = text.lower()
text = re.findall(r"[\d\w']+",text)
res = []
	for w in text:
		if w not in stopwords:
			res.append(w)
			
res

  





def tokenize(text,stopwords=[]):
    '''this function tokenizes `text` using simple rules:
    tokens are defined as maximal strings of letters, digits
    and apostrophies.
    The optional argument `stopwords` is a list of words to
    exclude from the tokenzation'''
    # make lowercase
    text = text.lower()
    # grab just the words we're interested in
    text = re.findall(r"[\d\w']+",text)
    # remove stopwords
    res = []
    for w in text:
        if w not in stopwords:
            res.append(w)
    
    return(res)