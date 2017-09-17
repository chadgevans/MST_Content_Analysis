import nltk
text=nltk.word_tokenize("The Dog chased the cat and the cat was mad.")
nltk.pos_tag(text)
nltk.corpus.floresta.raw()
#nltk.corpus.floresta.words()
#nltk.corpus.floresta.sents()
#nltk.corpus.floresta.tagged_words()
#nltk.corpus.floresta.tagged_sents()
#nltk.corpus.floresta.parsed_sents()
# the other tagged Portugues doc: nltk.corpus.mac_morpho.raw()
tagged_token=nltk.tag.str2tuple('grand/JJ') # this returs the x as a tuple
nltk.corpus.floresta.tagged_words()
from nltk.corpus import mac_morpho # mac morpho is portuguese
from nltk.corpus import floresta
?floresta.tagged_words
?mac_morpho.tagged_words
floresta_tagged=floresta.tagged_words(simplify_tags=True) #I simplified the tages
tag_fd=nltk.FreqDist(tag for (word,tag) in floresta_tagged)
tag_fd.keys()
#tag_fd.plot(cumulative=True) # this takes so long (I force quitted at 10 minutes)
nltk.app.concordance() 
word_tag_pairs=nltk.bigrams(floresta_tagged)
list(nltk.FreqDist(a[1] for (a,b) in word_tag_pairs if b[1]=='H')) #H is noun
wsj=nltk.corpus.floresta.tagged_words(simplify_tags=True)
word_tag_fd=nltk.FreqDist(wsj)
[word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('A')]

# Frequency-ordeded list of tags given a word (I used 'terra' and 'educação')
cfd1=nltk.ConditionalFreqDist(wsj)
cfd1['terra'].keys() # H, P
cfd1['educação'].keys() # NA

# tag is condition, word event: likely words for a given tag
cfd2=nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
cfd2['A'].keys()

idx1=wsj.index(('terra','H'))
wsj[idx1-4:idx1+1]

# idx2=wsj.index(('terra','A')) This wasn't in the list
# wsj[idx2-4:idx2+1]

def	findtags(tag_prefix, tagged_text): # I had to enter in line by line
	cfd= nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
								 if tag.startswith(tag_prefix))
	return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())
	
tagdict=findtags('H',nltk.corpus.floresta.tagged_words())
for tag in sorted(tagdict):
 print tag, tagdict[tag] #you may need to add this one like that to!
 
floresta_learned_text=floresta.words()
sorted(set(b for (a, b) in nltk.ibigrams(floresta_learned_text) if a == 'terra'))

floresta_lrnd_tagged = floresta.tagged_words()
tags= [b[1] for (a, b) in nltk.ibigrams(floresta_lrnd_tagged) if a[0] == 'terra']
fd=nltk.FreqDist(tags)
fd.tabulate() #most high frequency POS following

from nltk.corpus import floresta
def	process(sentance):
	for (w1, t1), (w2,t2), (w3,t3) in nltk.trigrams(sentance):
		if (t1.startswith('A') and t2 == 'para' and t3.startswith('A')):
			print w1, w2, w3
for tagged_sent in floresta.tagged_sents():
	process(tagged_sent) # this didn't work for me



