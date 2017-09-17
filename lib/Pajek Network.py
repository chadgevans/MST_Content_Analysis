from CA import *

#the default is it will drop stopwords and create a single pajek .net file.
#type doc_pajek_files? for more options

corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/PE_Clean')    #you can also use loadcorpus3b
a=doc_pajek_files(corpus, 'PENet')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/VP_Clean')
a=doc_pajek_files(corpus, 'VPNet')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/SEnter_Clean')
a=doc_pajek_files(corpus, 'SEnterNet')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/SInn_Clean')
a=doc_pajek_files(corpus, 'SInnNet')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/SEntrep_Clean')
a=doc_pajek_files(corpus, 'SEntrepNet')
corpus=loadcorpus2b('c://Users/jsradford/Desktop/Computing/CA Scripts/All')
a=doc_pajek_files(corpus, 'AllNet')
#BELOW ARE TESTS FOR ANOTHER RELATED NETWORK FUNCTION: CHUNK_PAJEK_FILES. PROBLEMS WITH TOKENIZING.

#postext=[]
#POSText=[]
#names=[]
##f = open(os.path.join('c:\\Users\jsradford\Desktop\Computing\CA Scripts\PE_Clean','r')
#        
#for k,v in dict.iteritems(corpus):
#    x=' '.join(v)
#    toks = nltk.word_tokenize(x)
#    text = nltk.text.Text(toks)
#    postext=nltk.tag.pos_tag(text)
#    POSText.append(postext)
#g=[]
#for v in POSText:
#    NameEnt=nltk.ne_chunk(v) 
#    y=NameEnt.productions()
#chunk_pajek_files(NameEnt, 'PEChunk',dropstops='yes')
#    
    #a=sorted(y)
    #print'writing NEs'
    #for i in range(0, len(a)-1):
    #    d=[]
    #    x=str(a[i])
    #    xsplt=x.split('(')
    #    del xsplt[0]
    #    for v in xsplt:
    #        c=v.split(',')
    #        d.append(c[0])
    #        e=' '.join(d)
    #    g.append(e)
#CURRENT PROBLEM: RESULTING NAMES LIST IS LIST OF TUPLES THAT HAVE TO MADE INTO STR
    
#a=nltk.corpus.stopwords.words('english')
#b=' '.join(a)
#stopw=b.split()


#first argument is the set of items to match files on - list of authors, topics, etc.
#the default is it will not drop stopwords and create a single pajek .net file.
#type chunk_pajek_files? for more options