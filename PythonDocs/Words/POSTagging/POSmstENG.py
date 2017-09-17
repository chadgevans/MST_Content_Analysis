import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy
import chunk
from nltk. chunk import tag_pattern2re_pattern
from nltk. chunk import RegexpParser
from nltk import bigrams
from nltk.probability import FreqDist
from nltk import trigrams
import pprint

# THIS IS Just Ten ENGLISH MST Articles 

f=open('/Users/chadgevans/Desktop/Justten.txt','r')
lines=f.readlines()

text=[]
for line in lines:
	line = line.rstrip()
	text.extend(nltk.word_tokenize(line))
	
clean_text=([w.lower() for w in text if w.isalpha()])
corpus10=clean_text
tagged=nltk.pos_tag(corpus10) # this takes 5-7 minutes

text=nltk.Text(word.lower() for word in corpus10)
text.similar('land')
text.similar('education')

tag_fd=nltk.FreqDist(tag for (word,tag) in tagged)
#tag_fd.keys() # all the tags i could choose['NN','IN','DT','NNS','JJ','CC','RB','VBD','VBN','TO','VB','VBZ','VBP','PRP','VBG','PRP$','MD','WDT','CD','JJR','WP','WRB','JJS','RP','RBR','EX','RBS','WP$','FW','PDT']
#nltk.help.upenn_tagset('CC') # to find out what POS symbols mean
#'NN' noun
#'IN' prep or conj
#'DT' determiner
#'NNS' noun plural
#'JJ' adjective
#'CC' conjunction
#'RB' adverb
#'VBD' verb past tense
#'VBN' verb past participle
#'TO' to, infinitive marker
#'VB' verb base for
#'VBZ' verb present tense, 3rd person
#'VBP' verb present tense, not 3rd person
#'PRP' pronoun, personal
#'VBG' verb, present participle or gerund
#'PRP$' possessive pronoun
#'MD' modal auxiliary # could be useful...commands
#'WDT' that what whatever which whichever WH-determiners
#'CD' numbers
#'JJR' comparative adjectives
#'WP' that what whatever whatsoever which who whom whosever WH-pronoun
#'WRB' how however, whence whenever, where whereby...Wh-adverb
#'JJS' superlative adjective
#'RP' particle: about, around, before...
#'RBR' comparative adverb: gloomier, graver, harder
#'EX' existential there
#'RBS' superlative adverb: biggest, less, most
#'WP$' Wh-pronoun, possessive: whose
#'FW' foreign word # could be useful looking for foreign words
#'PDT' predeterminer: all both, half, many, sure such, this
#tag_fd.plot(cumulative=True)# plots POS graph, not all that interesting

#nltk.app.concordance() how should this be formatted?

word_tag_pairs = nltk.bigrams(tagged)
list(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'NN')) #shows most frequent nouns coming before a verb

#most common verbs
word_tag_fd = nltk.FreqDist(tagged)
[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')] #somewhat interesing, what comes before verbs

#cfd1 = nltk.ConditionalFreqDist(tagged)
#cfd1['school'].keys() #not useful

cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged) 
cfd2['NN'].keys() #I'm not sure what this accomplished, but lots of nouns




# Preprocessing function to tdo this in the future.
def ie_preprocess(document):#tokenizes and tags all in one
	sentences = nltk.sent_tokenize(document)
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]

print sentences

#function for finding the most frequent tags
def findtags(tag_prefix, tagged_text): 
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
	return dict((tag, cfd[tag].keys()[:15]) for tag in cfd.conditions())

tagdict=findtags('NN',tagged) # most frequent noun tags
for tag in sorted(tagdict):
	print tag, tagdict[tag] # not too surprising, this looks like other functions that found most recurrent words

tagdict=findtags('VB',tagged) # common verb base
for tag in sorted(tagdict):
	print tag, tagdict[tag] # interesting...there are verbs of interest here

tagdict=findtags('JJS',tagged) # common superlatives
for tag in sorted(tagdict):
	print tag, tagdict[tag] # intersting


# Let the chunking begin
# Some Rules you can choose:
#NP: {<DT>?<JJ>*<NN>}
#{<NNP>+} match on one or more proper nouns
#{<JJ>?<NN>*} my creation, modified noun
#NP: {<DT|JJ|NN.*>+} chunk sequences of DT, JJ, NN
#PP: {<IN><NP>} chunnk prepositions followed by NP
#VP: {<VB.*><NP|PP|CLAUSE>+$} Chunk verbs and their arguments
#CLAUSE: {<NP><VP>} Chunk NP, VP


# Noun Phrases Chunking
sentence=tagged
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print result # this works, but big
# result.draw() I haven't tried to model it, too big

# Match on optional determiner or possessive pronoun, zero or more adjectives, then a noun
# Then match on one or more proper nouns
grammar = r"""
NP: {<DT|PP\$>?<JJ>*<NN>}
{<NNP>+}
"""
cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print cp.parse(sentence)

sample="The cow jumped over the moon.  It was made of cheese."
tokened = nltk.word_tokenize(sample)
tpsample=nltk.pos_tag(tokened)
grammar = r"""
NP: {<JJ>?<NN>*}
"""
cp = nltk.RegexpParser(grammar)
result = cp.parse(tpsample)[:10] # just first 10 words
print cp.parse(tpsample)[:10] #just first 10 words


# chunk it all: NP: {<.*>+}


# Searching Trigrams
def process(sentence): # function for searching trigrams
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print w1, w2, w3

process(tagged)

# another function to look for adv, adj followed by noun
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('RB') and t2 == 'JJ' and t3.startswith('N')):
            print w1, w2, w3

process(tagged)

# This one looks at Adv to Adjectives to Nouns
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1=='RB' and t2 == 'JJ' and t3.startswith('N')):
            print w1, w2, w3

process(tagged)

# let's see if this works with bigrams, it does!  but i only can get it to work on TAGs (not spec. nouns)
def process2(sentence):
    for (w1,t1), (w2,t2) in nltk.ibigrams(sentence):
        if (t1.startswith('N') and t2.startswith('V')):
            print w1, w2
process2(tagged)

#Looking for Tagged entities in a text, first 50
sent = tagged[:50] #first 10 named entities
print nltk.ne_chunk(sent, binary=True) #named entity function
#This works rather poorly


# Moving from abstract chunking to specific queries
cstand=nltk.RegexpParser(chunks_standard)
clarge=nltk.RegexpParser(chunks_large)
csents=nltk.RegexpParser(chunks_sents)

#Treestand
##this shows the chunk tree structure
#only do it if your texts aren't enormous
treestand=cstand.parse(tagged)
treelarge=clarge.parse(tagged)
treesents=csents.parse(tagged)

chunk_sim(treestand,'education') #words that show up in noun phrases with 'education'

chunk_sim(treelarge,'education')
#this shows all words in the larger chunks 
#that appear in phrases with 'education'

chunk_simpos(treelarge,'education','JJ')
#this shows all adjectives (e.g., JJ) 
#that appear in noun phrases with 'education'

