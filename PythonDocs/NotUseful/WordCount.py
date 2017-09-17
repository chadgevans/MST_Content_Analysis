# import what we'll need
import codecs
import re
import os
import sys
import scipy

import fnmatch

## define the functions that do the main work.

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


def make_tfidf(corpus , minFreq=3 , maxFreq=0.8 , dfExp=-0.5 , norm=True,stopwords=[]):
    '''this function takes `corpus`, a list of character strings, and returns
    a df-idf vectorization of the corpus.
    Any terms occurring in fewer than `minFreq` of the documents are thrown out,
    as are any terms in more than `maxFreq` proportion of the documents.
    The `dfExp` argument is the exponent on the document frequency, so leaving
    it at -0.5 uses the inverse square root.
    If `norm` is True (the default) then the vectors are normalized.
    Any terms in `stopwords` are removed from the vectorization.
    The return value is a tuple containing the names of the dimensions and
    an n-by-m matrix containing the document vectors, where n is the number
    of documents and m is the number of terms in the vectors.'''
    print('tokenizing')
    sys.stdout.flush() # this just makes sure that things get printed even if it's busy
    termsList = []
    for doc in corpus:
        # simply tokenize each each document
        termsList.append(tokenize(doc,stopwords=stopwords))