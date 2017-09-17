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
    
    print('creating vectors')
    sys.stdout.flush()
    # get the unique dimensions:
    allTerms = set() # sets are like unordered lists that don't allow duplicate entries
    for terms in termsList:
        allTerms.update(terms) # update method just adds `terms` to `allTerms`
    allTerms = list(allTerms) # convert to an order-preserving list
    allTermsDict = dict( zip( allTerms, range(len(allTerms)) ) ) # and make a dict to look up indices
    # build the frequency matrix, starting with a matrix of zeroes
    vs = scipy.zeros( ( len(corpus) , len(allTerms) ) ,dtype='float64')
    for i,terms in enumerate(termsList):
        print('vectorizing document '+str(i))
        sys.stdout.flush()
        for t in terms:
            vs[i,allTermsDict[t]]+=1 #increment the appropriate element of the matrix
    # get rid of terms that are too frequent or not frequent enough
    termFreqs = scipy.sum(vs>0 , 0) # this is just the frequencies
    keepTerms = (termFreqs >= minFreq)  &  (termFreqs < len(corpus)*maxFreq)
    vs = vs[:,keepTerms]
    allTerms = scipy.array(allTerms)[keepTerms] # need to truncate our names list too
    # multiply by inverse doc frequency
    idf = scipy.sum( vs>0 , 0) ** dfExp
    vs = vs * idf
    # normalize
    if norm:
    	print "vs is ", vs
        sumSqrs = scipy.sum(vs**2,1)
        magn = scipy.sqrt(sumSqrs)
        print "magn is calculated as ", magn
        magn = magn.reshape(len(corpus),1)
        print "trying to divide vs=%s by magn=%s" % (str(vs), str(magn))
        vs = vs/magn
    return(allTerms,vs)


## now load the documents to vectorize them (1867)
##
## these files each contain the speaker, a speech title, and the transcript of the speech
## my corpus is just the transcripts, but the speakers and titles are useful metadata
## so I make a list for each of these.
speakers = []
titles = []
corpus = []
for fn in os.listdir('/Users/chadgevans/Desktop/PythonDocs/MSTCorpus'):
	print "we are opening filename ", fn
	if (fnmatch.fnmatch(fn, '*.txt')):
		f = open('/Users/chadgevans/Desktop/PythonDocs/MSTCorpus/'+fn,'r')
		text = f.read()
		corpus.append(text)

terms,vs = make_tfidf(corpus) # this runs the functions above on our corpus

f = open('MSTCorpus.txt','w')
f.write('\t'.join(terms) + '\n')
for i in xrange(vs.shape[0]):
   
    
    
    vec = vs[i,]
    f.write('\t'.join(vec.astype('S50')) + '\n')
f.close() #2150-