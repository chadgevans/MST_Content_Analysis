import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy
import chunk
from nltk.corpus import wordnet as wn
from nltk. chunk import tag_pattern2re_pattern
from nltk. chunk import RegexpParser
from nltk import bigrams
from nltk.probability import FreqDist
from nltk import trigrams
import pprint
import fnmatch

#############################################################
#                English Corpus Summaries
#############################################################
# Loading the corpus
f=open('/Users/chadgevans/Desktop/MSTEnglishCorpus.txt','r')
lines=f.readlines()

Rawtext=[]
for line in lines:
	line = line.rstrip()
	Rawtext.extend(nltk.word_tokenize(line))
	
len(Rawtext) # 575,207 tokens
len(set(Rawtext)) # number of word types 41,358

# Cleaning the text
stopwords = nltk.corpus.stopwords.words('english')
text = []
for w in Rawtext:
	if w not in stopwords:
		text.append(w)

clean_text=([w.lower() for w in text if w.isalpha()])
clean_text_set=set([w.lower() for w in text if w.isalpha()])
corpus=clean_text

#Basic Word Statistics
len(corpus) # 259,116
len(clean_text_set) # 23,702

##########################################################
#      English - Exploring the words in the text
########################################################
# Highest Word Counts
fdist=FreqDist(corpus)
fdist
vocabulary=fdist.keys()
vocabulary[:25]
# Plotted
fdist.plot(20,cumulative=True)

# Important words?  Considering length and frequency
longw=[word for word in corpus if len(word)>10] # just length
sorted(longw)
# the words below are longer AND frequent; they may be important
sorted([w for w in set(corpus) if len(w)>7 and fdist[w]>7])

# Are there unusual words in my corpus?  Let's compare it to nltk's corpus
def unusual_words(corpus):
	text_vocab=set(w.lower() for w in clean_text if w.isalpha())
	english_vocab=set(w.lower() for w in nltk.corpus.words.words())
	unusual = text_vocab.difference(english_vocab)
	return sorted(unusual)

unusual_words(corpus)

NLTKText=nltk.text.Text(corpus)
NLTKText.collocations()

######################################################
#         English - Pre-defined Words of Interest
#####################################################
# Using Python tools to investigate words of interest

# Specific Word Counts
corpus.count("land") #2697
corpus.count("education") #329
corpus.count("access") #319
corpus.count("feminism") #15
corpus.count("movement") #1833
corpus.count("rights") #380
corpus.count("oppression") #8
corpus.count("struggle") #494

# The context of words of interest
NLTKText=nltk.text.Text(corpus)
NLTKText.concordance("land")
NLTKText.concordance("fight")
NLTKText.concordance("state")
NLTKText.concordance("social")
NLTKText.concordance("education")

NLTKText.similar("land")
NLTKText.similar("fight")
NLTKText.similar("health")
NLTKText.similar("feminism")
NLTKText.similar("education")

NLTKText.common_contexts(["land","agrarian"])
NLTKText.common_contexts(["land","education"])
NLTKText.common_contexts(["land","fight"])
NLTKText.common_contexts(["land","women"])
NLTKText.common_contexts(["health","women"])
NLTKText.common_contexts(["land","agrarian","rural"])

NLTKText.dispersion_plot(["education","land","political","reform","rural","work","fight","agrarian","state"])

# Using N-Grams
bigrams(corpus) #bigrams
trigrmas(corpus) #trigrams

# Bigrams and Conditional Frequency Distributions following words of interest 
bigrams=nltk.bigrams(corpus)
cfd=nltk.ConditionalFreqDist(bigrams)
print cfd['education']
print cfd['land']
print cfd['school']
print cfd['women']
print cfd['struggle']
print cfd['political']
print cfd['state']
print cfd['rural']
print cfd['access']

sorted(set(b for (a, b) in nltk.bigrams(corpus) if a == 'never')) # interesting (you can use ibigrams or bigrams)
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'sometimes')) # interesting
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'must')) # 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'should')) # 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'terrorist')) # 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'capitalism')) # 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'fair')) # 

#############################################################
#                Portuguese Corpus Summaries
#############################################################
f=open('/Users/chadgevans/Desktop/PurgedMSTBrazilCorpus.txt','r')
lines=f.readlines()

Brawtext=[]
for line in lines:
	line = line.rstrip()
	Brawtext.extend(nltk.word_tokenize(line))

len(Brawtext) # 1,079,548
len(set(Brawtext)) # number of word types 52,774

# cleaning the text
stopwords=['de','a','o','que','e','do','da','em','um','para','com','n√£o','uma','os','no','se','na','por','mais','as','dos','como','mas','ao','ele','das','√†','seu','sua','ou','quando','muito','nos','j√°','eu','tamb√©m','s√≥','pelo','pela','at√©','isso','ela','entre','depois','sem','mesmo','aos','seus','quem','nas','me','esse','eles','voc√™','essa','num','nem','suas','meu','√†s','minha','numa','pelos','elas','qual','n√≥s','lhe','deles','essas','esses','pelas','este','dele','tu','te','voc√™s','vos','lhes','meus','minhas','teu','tua','teus','tuas','nosso','nossa','nossos','nossas','dela','delas','esta','estes','estas','aquele','aquela','aqueles','aquelas','isto','aquilo','estou','est√°','estamos','est√£o','estive','esteve','estivemos','estiveram','estava','est√°vamos','estavam','estivera','estiv√©ramos','esteja','estejamos','estejam','estivesse','estiv√©ssemos','estivessem','estiver','estivermos','estiverem','hei','h√°','havemos','h√£o','houve','houvemos','houveram','houvera','houv√©ramos','haja','hajamos','hajam','houvesse','houv√©ssemos','houvessem','houver','houvermos','houverem','houverei','houver√°','houveremos','houver√£o','houveria','houver√≠amos','houveriam','sou','somos','s√£o','era','√©ramos','eram','fui','foi','fomos','foram','fora','f√¥ramos','seja','sejamos','sejam','fosse','f√¥ssemos','fossem','for','formos','forem','serei','ser√°','seremos','ser√£o','seria','ser√≠amos','seriam','tenho','tem','temos','t√©m','tinha','t√≠nhamos','tinham','tive','teve','tivemos','tiveram','tivera','tiv√©ramos','tenha','tenhamos','tenham','tivesse','tiv√©ssemos','tivessem','tiver','tivermos','tiverem','terei','ter√°','teremos','ter√£o','teria','ter√≠amos','teriam']
Btext = []
for w in Brawtext:
	if w not in stopwords:
		Btext.append(w)

Bclean_text=([w.lower() for w in Btext if w.isalpha()])
Bclean_text_set=set([w.lower() for w in Btext if w.isalpha()])
Bcorpus=Bclean_text

#Basic Word Statistics
len(Bcorpus) # 418,722
len(Bclean_text_set) # 32,611

##########################################################
#      Portuguese - Exploring the words in the text
########################################################
# Using Python tools to investigate words of interest

fdist=FreqDist(Bcorpus) # this jams if not entered line by line
fdist
vocabulary=fdist.keys()
vocabulary[:25]
fdist.plot(50,cumulative=True)

longw=[word for word in Bcorpus if len(word)>10]
sorted(longw) # lengthy not all that important, more important freq
sorted([w for w in set(Bcorpus) if len(w)>8 and fdist[w]>250]) #these words are longer and yet frequent

bigrams(Bcorpus) #to look at just all bigrams
trigrmas(Bcorpus)

#def unusual_words(Bcorpus): (only comparing with nltk english words)
#	text_vocab=set(w.lower() for w in Bclean_text if w.isalpha())
#	english_vocab=set(w.lower() for w in nltk.corpus.words.words())
#	unusual = text_vocab.difference(english_vocab)
#	return sorted(unusual)
	
unusual_words(Bcorpus)

NLTKText=nltk.text.Text(Bcorpus)
NLTKText.collocations()

######################################################
#      Portuguese - Pre-defined Words of Interest
#####################################################
# Specific Word Counts
Bcorpus.count("terra") # 1931
Bcorpus.count("educa") # 2027
Bcorpus.count("acesso") # 299
Bcorpus.count("feminismo") # 0
Bcorpus.count("movimento") # 1786
Bcorpus.count("direito") # 206
Bcorpus.count("capitalismo") # 101
Bcorpus.count("luta") # 901

# The context of words of interest
NLTKText=nltk.text.Text(Bcorpus)
NLTKText.concordance("terra")
NLTKText.concordance("luta")
NLTKText.concordance("movimento")
NLTKText.concordance("social")
NLTKText.concordance("educa")
NLTKText.concordance("estado")

NLTKText.similar("terra")
NLTKText.similar("luta")
NLTKText.similar("sa")
NLTKText.similar("feminista")
NLTKText.similar("educa")

NLTKText.common_contexts(["terra","agr"])
NLTKText.common_contexts(["terra","educa"])
NLTKText.common_contexts(["terra","fight"])
NLTKText.common_contexts(["terra","mulheres"])
NLTKText.common_contexts(["sa","mulheres"])
NLTKText.common_contexts(["terra","agr","campo"])

NLTKText.dispersion_plot(["educa","terra","pol","reforma","campo","trabalho","luta","agr","estado"])

# Using N-Grams
bigrams(Bcorpus) #bigrams
trigrmas(Bcorpus) #trigrams

# Bigrams and Conditional Frequency Distributions following words of interest 
bigrams=nltk.bigrams(Bcorpus)
cfd=nltk.ConditionalFreqDist(bigrams)
print cfd['educa']
print cfd['terra']
print cfd['escola']
print cfd['mulheres']
print cfd['luta']
print cfd['pol']
print cfd['estado']
print cfd['campo']
print cfd['acesso']

sorted(set(b for (a, b) in nltk.bigrams(corpus) if a == 'never')) 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'sometimes'))
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'must'))
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'should')) 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'terrorist')) 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'capitalism')) 
sorted(set(b for (a, b) in nltk.ibigrams(corpus) if a == 'fair'))


#############################################################
#    POS Tagging - Random Sample of 10 English MST texts
#############################################################
# Summary Statistics
# This is a random sample of the 52 article corpus
f=open('/Users/chadgevans/Desktop/Justten.txt','r')
lines=f.readlines()

# stopwords retained
Ttext=[]
for line in lines:
	line = line.rstrip()
	Ttext.extend(nltk.word_tokenize(line))

len(Ttext) # 136,307
len(set(Ttext)) # number of word types 16,423

# clean the text (but leaving in stopwords!)
Tclean_text=([w.lower() for w in Ttext if w.isalpha()])
Tclean_text_set=set([w.lower() for w in Ttext if w.isalpha()])
Tcorpus=Tclean_text

#Basic Word Statistics
len(Tcorpus) # 102,500
len(Tclean_text_set) # 10,456

#######################################################
#               POS taggging
#######################################################
tagged=nltk.pos_tag(Tcorpus) # this takes 5-7 minutes

# POS basics
tag_fd=nltk.FreqDist(tag for (word,tag) in tagged)
tag_fd.keys()
nltk.help.upenn_tagset('CC') # to find out what POS symbols mean
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

#function for finding the most frequent POS (e.g. noun) for each POS type
def findtags(tag_prefix, tagged_text): 
	cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
	return dict((tag, cfd[tag].keys()[:25]) for tag in cfd.conditions())

tagdict=findtags('VBZ',tagged) # 25 most frequent third person verbs
for tag in sorted(tagdict):
	print tag, tagdict[tag]

tagdict=findtags('JJ',tagged) # 25 most frequent adjectives
for tag in sorted(tagdict):
	print tag, tagdict[tag] 

tagdict=findtags('JJR',tagged) # 25 most frequent comparative adjectives
for tag in sorted(tagdict):
	print tag, tagdict[tag]

tagdict=findtags('JJS',tagged) # 25 most frequent adjective superlatives
for tag in sorted(tagdict):
	print tag, tagdict[tag]

###############################################################
#				  Chunking the sample
###############################################################
# Some Rules you can choose from:
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
print result

#       Words and their contexts
# functions
cstand=nltk.RegexpParser(chunks_standard)
clarge=nltk.RegexpParser(chunks_large)
csents=nltk.RegexpParser(chunks_sents)
treestand=cstand.parse(tagged)
treelarge=clarge.parse(tagged)
treesents=csents.parse(tagged)

# what shows up in noun phrases with the word'
e=chunk_sim(treestand,'education')#length 141
c=chunk_sim(treestand,'children')#length 40
sc=chunk_sim(treestand,'schools')#length 27


#What verbs and adjectives are happening around the word?
evbz=chunk_simpos(treestand,'education','VBZ')#0
ejj=chunk_simpos(treestand,'education','JJ')# 30, many hits, but political, technical,and economic

cvbz=chunk_simpos(treestand,'children','VBZ')#0
cjj=chunk_simpos(treestand,'children','JJ')# 6

scvbz=chunk_simpos(treestand,'schools','VBZ')#0
sjj=chunk_simpos(treestand,'schools','JJ')#10, democratic, publc, but not children or pedagogy





###########################################################
#                     Vectorizing
###########################################################


# First the English MST Texts
# Tokenize
def tokenize(text,stopwords=[]):
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

# TF-IDF
def make_tfidf(corpus , minFreq=3 , maxFreq=0.8 , dfExp=-0.5 , norm=True,stopwords=[]):
    
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

# Import, Vectorize and Export my English MST Corpus
for fn in os.listdir('/Users/chadgevans/Desktop/PythonDocs/MSTFiles/MSTEnglishCorpus'):
	print "we are opening filename ", fn
	if (fnmatch.fnmatch(fn, '*.txt')):
		f = open('/Users/chadgevans/Desktop/PythonDocs/MSTFiles/MSTEnglishCorpus/'+fn,'r')
		text = f.read()
		corpus.append(text)

terms,vs = make_tfidf(corpus) # this runs the functions above on our corpus

f = open('VectMSTengCorpus.txt','w')
f.write('\t'.join(terms) + '\n')
for i in xrange(vs.shape[0]):
   
    
    
    vec = vs[i,]
    f.write('\t'.join(vec.astype('S50')) + '\n')
f.close() 



# Loading, Vectorizing and Exporting My Portuguese Texts
for fn in os.listdir('/Users/chadgevans/Desktop/PythonDocs/MSTFiles/MSTBrazilCorpus'):
	print "we are opening filename ", fn
	if (fnmatch.fnmatch(fn, '*.txt')):
		f = open('/Users/chadgevans/Desktop/PythonDocs/MSTFiles/MSTBrazilCorpus/'+fn,'r')
		text = f.read()
		corpus.append(text)

terms,vs = make_tfidf(corpus) # this runs the functions above on our corpus

f = open('VectMSTbrazCorpus.txt','w')
f.write('\t'.join(terms) + '\n')
for i in xrange(vs.shape[0]):
   
    
    
    vec = vs[i,]
    f.write('\t'.join(vec.astype('S50')) + '\n')
f.close() 