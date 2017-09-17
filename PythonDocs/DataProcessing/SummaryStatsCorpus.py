import nltk
import pylab
from CA import *
import codecs
import re
import os
import sys
import scipy

f=open('/Users/chadgevans/Desktop/PythonDocs/DataProcessing/Corpus.txt','r')
lines=f.readlines()

MST_tokens = []
for line in lines:
	line = line.rstrip() 
	MST_tokens.extend(nltk.word_tokenize(line))

text=MST_tokens

stopwords=['de','a','o','que','e','do','da','em','um','para','com','n√£o','uma','os','no','se','na','por','mais','as','dos','como','mas','ao','ele','das','√†','seu','sua','ou','quando','muito','nos','j√°','eu','tamb√©m','s√≥','pelo','pela','at√©','isso','ela','entre','depois','sem','mesmo','aos','seus','quem','nas','me','esse','eles','voc√™','essa','num','nem','suas','meu','√†s','minha','numa','pelos','elas','qual','n√≥s','lhe','deles','essas','esses','pelas','este','dele','tu','te','voc√™s','vos','lhes','meus','minhas','teu','tua','teus','tuas','nosso','nossa','nossos','nossas','dela','delas','esta','estes','estas','aquele','aquela','aqueles','aquelas','isto','aquilo','estou','est√°','estamos','est√£o','estive','esteve','estivemos','estiveram','estava','est√°vamos','estavam','estivera','estiv√©ramos','esteja','estejamos','estejam','estivesse','estiv√©ssemos','estivessem','estiver','estivermos','estiverem','hei','h√°','havemos','h√£o','houve','houvemos','houveram','houvera','houv√©ramos','haja','hajamos','hajam','houvesse','houv√©ssemos','houvessem','houver','houvermos','houverem','houverei','houver√°','houveremos','houver√£o','houveria','houver√≠amos','houveriam','sou','somos','s√£o','era','√©ramos','eram','fui','foi','fomos','foram','fora','f√¥ramos','seja','sejamos','sejam','fosse','f√¥ssemos','fossem','for','formos','forem','serei','ser√°','seremos','ser√£o','seria','ser√≠amos','seriam','tenho','tem','temos','t√©m','tinha','t√≠nhamos','tinham','tive','teve','tivemos','tiveram','tivera','tiv√©ramos','tenha','tenhamos','tenham','tivesse','tiv√©ssemos','tivessem','tiver','tivermos','tiverem','terei','ter√°','teremos','ter√£o','teria','ter√≠amos','teriam']
res = []
	for w in text:
		if w not in stopwords:
			res.append(w)
	
text=res

#Basic Word Statistics
len(text) # number of tokens (957,525 on 3/14)
clean_text=([w.lower() for w in text if w.isalpha()]) 
len(clean_text) #(479,580 on 3/14)

len(set(text)) # number of word types (53,255 on 3/14)
#sorted(set(text)) # sorted vocabulary, good place to check words of interest
clean_text_set=set([w.lower() for w in text if w.isalpha()]) # cleaned so only alpha and lower
len(clean_text_set) # 32,861 on 3/14



