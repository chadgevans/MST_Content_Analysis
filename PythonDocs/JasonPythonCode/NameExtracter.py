import nltk
import pylab
import re
import os
import sys
from CA import *

def NameExtract(dirname,fname):
    '''define directory where files are located and custom name files should be saved as'''
    names=[]
    name=[]
    outfile=open(fname+'names.txt', 'w')
    #texts = {}
    fnames = [fn for fn in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, fn))]
    for fn in fnames:
        f = open(os.path.join(dirname,fn), 'r')
        raw = f.read()
        toks = nltk.word_tokenize(raw)
        text = nltk.text.Text(toks)         #imported each file individually and tokenized
        #texts[fname] = text
                                            #Next, is the function I'm running on each file.  In this case, POSTagger and Named Entity Chunker
        g=[]
        POSText=nltk.tag.pos_tag(text)
        NameEnt=nltk.ne_chunk(POSText)        #tags named entities, returns tree objects and tuples (trees are NEs)
        y=NameEnt.productions()
        a=sorted(y)
        print'writing NEs'
        for i in range(0, len(a)-1):
            d=[]
            x=str(a[i])
            xsplt=x.split('(')
            del xsplt[0]
            for v in xsplt:
                c=v.split(',')
                d.append(c[0])
                e=' '.join(d)
            g.append(e)
        print 'appending ngrams'
        name.append(g)
    m=str(name)                             #I've appended the NE Chunker to a list (names) and am writing it to a file (here a string b/c I can't figure out writelines())
    outfile.write(m)                        #Note, I'm not in the 'for fn in fnames' loop, so I'm creating a single file with all of the names
    outfile.close()

NameExtract('c:\\Users\jsradford\Desktop\Computing\CA Scripts\PE_Clean','PE')
NameExtract('c:\\Users\jsradford\Desktop\Computing\CA Scripts\SEnter_Clean','SEnter')
NameExtract('c:\\Users\jsradford\Desktop\Computing\CA Scripts\SEntrep_Clean','SEntrep')
NameExtract('c:\\Users\jsradford\Desktop\Computing\CA Scripts\VP_Clean','VP')
NameExtract('c:\\Users\jsradford\Desktop\Computing\CA Scripts\SInn_Clean','SInn')
