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
from nltk import trigrams
from nltk.corpus import wordnet as wn

# THIS IS THE ENGLISH MST CORPUS 

stopwords = nltk.corpus.stopwords.words('english')
f=open('/Users/chadgevans/Desktop/MSTEnglishCorpus.txt','r')
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
len(text) # number of tokens (408,232 on 3/15)
clean_text=([w.lower() for w in text if w.isalpha()])
len(clean_text) #(259,116 on 3/15)

len(set(text)) # number of word types (41,358 on 3/15)
#sorted(set(text)) # sorted vocabulary, good place to check words of interest
clean_text_set=set([w.lower() for w in text if w.isalpha()]) # cleaned so only alpha and lower
len(clean_text_set) # 23702 on 3/15

corpus=clean_text

len(corpus)
len(set(corpus))
#sorted(set(corpus))

fdist=FreqDist(corpus) # this jams if not entered line by line, b/c of corpus
fdist
vocabulary=fdist.keys()
vocabulary[:25]
fdist.plot(20,cumulative=True)

longw=[word for word in corpus if len(word)>10]
sorted(longw) # lengthy not all that important, more important freq
sorted([w for w in set(corpus) if len(w)>7 and fdist[w]>7]) #these words are longer and yet frequent

bigrams(corpus) #to look at just all bigrams
trigrmas(corpus)

def unusual_words(corpus):
	text_vocab=set(w.lower() for w in clean_text if w.isalpha())
	english_vocab=set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)
	
unusual_words(corpus)

wn.synsets('land') # synonyms
wn.synset('land.n.02').lemma_names
wn.synset('land.n.02').definition # actual meaning of it
wn.synset('land.n.02').examples #some examples
wn.lemma('worker.n.01.worker').antonyms() #antonyms


#Playing with specific words
corpus.count("land") #Put in words of interest here!!!

NLTKText=nltk.text.Text(corpus)
NLTKText.concordance("land") 
NLTKText.similar("land")
NLTKText.common_contexts(["land","agrarian"])
NLTKText.dispersion_plot(["education","land","political","reform","rural","work","fight","agrarian","state"])
NLTKText.collocations()

bigrams=nltk.bigrams(corpus)
cfd=nltk.ConditionalFreqDist(bigrams)
print cfd['education']
print cfd['land']
print cfd['school']

#ConditionalFreqDist THIS DID NOT WORK!!!
#cfd=nltk.ConditionalFreqDist(
#	(target, file[:4])
#	for fileid in inaugural.fileids()
#	for w in inaugural.words(fileid)
#	for target in ['america','citizen']
#	if w.lower().startswith(target))
#cfd.plot() # gives conditional freq distribution of words 'america' and 'citizen' with different years


sorted(set(b for (a, b) in nltk.bigrams(corpus10) if a == 'never')) # interesting (you can use ibigrams or bigrams)
sorted(set(b for (a, b) in nltk.ibigrams(corpus10) if a == 'sometimes')) # interesting

#this doesn't work
tags = [b[1] for (a, b) in nltk.ibigrams(corpus10) if a[0] == 'never']
fd = nltk.FreqDist(tags)
fd.tabulate() # it doesn't kick out anything
 
