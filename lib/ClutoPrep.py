import nltk
from CA import *

corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/PE_Clean')
doc_cluto_files(corpus, "PECluto")
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/VP_Clean')
doc_cluto_files(corpus, "VPCluto")
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/SEnter_Clean')
doc_cluto_files(corpus, 'SEnterCluto')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/SInn_Clean')
doc_cluto_files(corpus, 'SInnCluto')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/SEntrep_Clean')
doc_cluto_files(corpus, 'SEntrepCluto')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/All')
doc_cluto_files(corpus, 'AllCluto')
