import nltk.corpus, nltk.tag, itertools
from nltk.tag import brill
# PRESS: REVIEWS
brownc_sents = nltk.corpus.brown.tagged_sents(categories="c")
# POPULAR LORE
brownf_sents = nltk.corpus.brown.tagged_sents(categories="f")
# FICTION: ROMANCE
brownp_sents = nltk.corpus.brown.tagged_sents(categories="p")	 

brown_train = list(itertools.chain(brownc_sents[:1000], 
brownf_sents[:1000], brownp_sents[:1000]))
brown_test = list(itertools.chain(brownc_sents[1000:2000], 
brownf_sents[1000:2000], brownp_sents[1000:2000]))
 
conll_sents = nltk.corpus.conll2000.tagged_sents()
conll_train = list(conll_sents[:4000])
conll_test = list(conll_sents[4000:8000])

treebank_sents = nltk.corpus.treebank.tagged_sents()
treebank_train = list(treebank_sents[:1500])
treebank_test = list(treebank_sents[1500:3000])