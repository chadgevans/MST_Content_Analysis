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

# THIS IS THE Portuguese MST CORPUS 

stopwords=['de','a','o','que','e','do','da','em','um','para','com','n√£o','uma','os','no','se','na','por','mais','as','dos','como','mas','ao','ele','das','√†','seu','sua','ou','quando','muito','nos','j√°','eu','tamb√©m','s√≥','pelo','pela','at√©','isso','ela','entre','depois','sem','mesmo','aos','seus','quem','nas','me','esse','eles','voc√™','essa','num','nem','suas','meu','√†s','minha','numa','pelos','elas','qual','n√≥s','lhe','deles','essas','esses','pelas','este','dele','tu','te','voc√™s','vos','lhes','meus','minhas','teu','tua','teus','tuas','nosso','nossa','nossos','nossas','dela','delas','esta','estes','estas','aquele','aquela','aqueles','aquelas','isto','aquilo','estou','est√°','estamos','est√£o','estive','esteve','estivemos','estiveram','estava','est√°vamos','estavam','estivera','estiv√©ramos','esteja','estejamos','estejam','estivesse','estiv√©ssemos','estivessem','estiver','estivermos','estiverem','hei','h√°','havemos','h√£o','houve','houvemos','houveram','houvera','houv√©ramos','haja','hajamos','hajam','houvesse','houv√©ssemos','houvessem','houver','houvermos','houverem','houverei','houver√°','houveremos','houver√£o','houveria','houver√≠amos','houveriam','sou','somos','s√£o','era','√©ramos','eram','fui','foi','fomos','foram','fora','f√¥ramos','seja','sejamos','sejam','fosse','f√¥ssemos','fossem','for','formos','forem','serei','ser√°','seremos','ser√£o','seria','ser√≠amos','seriam','tenho','tem','temos','t√©m','tinha','t√≠nhamos','tinham','tive','teve','tivemos','tiveram','tivera','tiv√©ramos','tenha','tenhamos','tenham','tivesse','tiv√©ssemos','tivessem','tiver','tivermos','tiverem','terei','ter√°','teremos','ter√£o','teria','ter√≠amos','teriam']

f=open('/Users/chadgevans/Desktop/MSTBrazilCorpus.txt','r')
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
len(text) # number of tokens (957,524 on 3/16)
clean_text=([w.lower() for w in text if w.isalpha()])
len(clean_text) #(479,580 on 3/16)

len(set(text)) # number of word types (53,255 on 3/16)
#sorted(set(text)) # sorted vocabulary, good place to check words of interest
clean_text_set=set([w.lower() for w in text if w.isalpha()]) # cleaned so only alpha and lower
len(clean_text_set) # 32,861 on 3/15

corpus=clean_text

len(corpus)
len(set(corpus))
#sorted(set(corpus))

fdist=FreqDist(corpus) # this jams if not entered line by line
fdist
vocabulary=fdist.keys()
vocabulary[:25]
fdist.plot(50,cumulative=True)

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
#round(((corpus.count("land"))/len(corpus))[,8]) I can't get this to work

NLTKText=nltk.text.Text(corpus)
NLTKText.concordance("land") 
NLTKText.similar("land")
NLTKText.common_contexts(["terra","campo"])
NLTKText.dispersion_plot(["educa","terra","pol","reforma","campo","trabalho","luta","agr","estado"])
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

