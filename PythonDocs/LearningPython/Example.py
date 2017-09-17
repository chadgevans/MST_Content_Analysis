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

# an example that works
from nltk.book import*
text1
text1.concordance("monstruous")
text1.similar("monstrous")

text2.common_contexts(["monstruous","very"])
text4.dispersion_plot(["citizens","democracy","freedom","duties","America"]) #THIS IS AWESOME
len(text4)
len(set(text1))
sorted(set(text1))

text5.count("lol")
100*text5.count('a')/len(text5)

fdist1=FreqDist(text1)
fdist1
vocabulary1=fdist1.keys()
vocabulary1[:25]
fdist1.plot(50,cumulative=True)

# What is text1 about?
#are all the words meaningful?

longw=[word for word in text1 if len(word)>10]
sorted(longw) # lengthy not all that important, more important freq

fdist5=FreqDist(text5)
sorted([w for w in set(text5) if len(w)>7 and fdist5[w]>7]) #these words are longer and yet frequent
sent=['near','river','bank'] # you would put in your tokenized set here
bigrams(sent)

#collocations
text4.collocations()


#ConditionalFreqDist THIS DID NOT WORK!!!
#cfd=nltk.ConditionalFreqDist(
#	(target, file[:4])
#	for fileid in inaugural.fileids()
#	for w in inaugural.words(fileid)
#	for target in ['america','citizen']
#	if w.lower().startswith(target))
#cfd.plot() # gives conditional freq distribution of words 'america' and 'citizen' with different years

# Here's a different example from book
from nltk.corpus import udhr
udhr.fileids()
languages = ['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
	(lang, len(word))
	for lang in languages
	for word in udhr.words(lang + '-Latin1'))
cfd.plot(cumulative=True)
#

generating text (applying bigrams)
def generate_model(cfdist,word,num=15):
for i in range(num):
	print word,
	word=cfdist[word].max()
	
text=nltk.corpus.genesis.words('english-kjv.txt')
bigrams=nltk.bigrams(text)
cfd=nltk.ConditionalFreqDist(bigrams)
print cfd['living']
generate_model(cfd,'living')

def unusual_words(text):
	text_vocab=set(w.lower() for w in text if w.isalpha())
	english_vocab=set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)
	
unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')) #also gives misspellings


#stopwords
from nltk.corpus import stopwords
stopwords.words('english')
#percent of content
def content_fraction(text):
	stopwords=nltk.corpus.stopwords.words('english')
	content=[w for w in text if w.lower() not in stopwords]
	return len(content)/len(text)
	
content_fraction(nltk.corpus.reuters.words()) # this is the useful fraction of useful words (equal to zero)

from nltk.corpus import wordnet as wn
wn.synsets('motorcar') # synonyms
wn.synset('car.n.01').lemma_names
wn.synset('car.n.01').definition # actual meaning of it
wn.synset('car.n.01').examples #some examples
wn.lemma('supply.n.02.supply').antonyms()



