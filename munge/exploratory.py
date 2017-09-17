import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy
from nltk.probability import FreqDist
from nltk import bigrams
from nltk.corpus import wordnet as wn

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
clean_text=([w.lower() for w in text if w.isalpha()])

corpus=clean_text

NLTKText=nltk.text.Text(clean_text)
NLTKText.concordance("land") 
NLTKText.similar("land")
NLTKText.common_contexts(["land","agrarian"])
NLTKText.dispersion_plot(["citizens","democracy","freedom","education","MST"])

len(corpus)
len(set(corpus))
sorted(set(corpus))

corpus.count("land") #Put in words of interest here!!!
100*corpus.count('land')/len(corpus) # percent of text land consists of

fdist=FreqDist(corpus)
fdist
vocabulary=fdist.keys()
vocabulary[:25]
fdist.plot(50,cumulative=True)

longw=[word for word in corpus if len(word)>10]
sorted(longw) # lengthy not all that important, more important freq
sorted([w for w in set(corpus) if len(w)>7 and fdist[w]>7]) #these words are longer and yet frequent

bigrams(corpus) #to look at just all bigrams

#collocations
NLTKText.collocations()  # I still cannot get collocations to work on the corpus "list"

#ConditionalFreqDist THIS DID NOT WORK!!!
#cfd=nltk.ConditionalFreqDist(
#	(target, file[:4])
#	for fileid in inaugural.fileids()
#	for w in inaugural.words(fileid)
#	for target in ['america','citizen']
#	if w.lower().startswith(target))
#cfd.plot() # gives conditional freq distribution of words 'america' and 'citizen' with different years
	
bigrams=nltk.bigrams(clean_text)
cfd=nltk.ConditionalFreqDist(bigrams)
print cfd['education']
print cfd['land']
print cfd['school']

def unusual_words(corpus):
	text_vocab=set(w.lower() for w in clean_text if w.isalpha())
	english_vocab=set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)
	
unusual_words(corpus) #also gives misspellings

wn.synsets('land') # synonyms
wn.synset('land.n.02').lemma_names
wn.synset('land.n.02').definition # actual meaning of it
wn.synset('land.n.02').examples #some examples
wn.lemma('worker.n.01.worker').antonyms() #antonyms


 
