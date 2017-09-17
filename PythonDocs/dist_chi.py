




import nltk, math
from operator import *

def do_tokenize(fname, form):
    if form=="text":
        f = open(fname)
        raw = f.read()
        sents = nltk.sent_tokenize(raw)
        fulltok = []
        for s in sents:
            tok=nltk.word_tokenize(s)
            fulltok += tok
        text = nltk.Text(fulltok)

    elif form=="corpus1":
        fulltok=corpus1.tokens
        text = nltk.Text(fulltok)

    elif form=="corpus2":
        fulltok=[]
        for fileid in fname.fileids():
            sents = fname.sents(fileid)
            for s in sents:
                fulltok += s
            text = nltk.Text(fulltok)
            
    else:
        print "put in texts or corpora"

    stopwords = nltk.corpus.stopwords.words('english')

    fulltok = [t.lower() for t in fulltok if t.lower() not in stopwords and t.lower().islower()]
    
    big = nltk.bigrams(fulltok)
    trig = nltk.trigrams(fulltok)
    return (text, big, trig)


def do_chi_square(phrase, f_p1_freqdist, f_p2_freqdist):
	f_p1 = f_p1_freqdist[phrase]
	f_notp1 = f_p1_freqdist.N() - f_p1_freqdist[phrase]

	f_p2 = f_p2_freqdist[phrase]
	f_notp2 = f_p2_freqdist.N() - f_p2_freqdist[phrase]

	# cf. Gentzkow and Shapiro p. 13
 	numerator = math.pow(((f_p1 * f_notp2) - (f_p2 * f_notp1)), 2)
	denominator = float((f_p1 + f_p2) *(f_p1 + f_notp1) * (f_p2 + f_notp2) *(f_notp1 + f_notp2))

	return float(numerator / denominator)


def distngrams(text1, text2, form):
	"""This creates a comparative analysis of distinguishing bi- and trigrams across two document sets.
	The first element and second arguments are texts, corpus1, or corpus2 of the loadcorpus1 or loadcorpus2 variety ('PlaintextCorpusReader'); 
	the third is a string--'text','corpus1', or 'corpus2' to indicate which.
	Two objects are returned: the sorted lists of distinguishing phrases for corpus 1 and 2"""
	
	old, oldb, oldt = do_tokenize(text1, form)
	new, newb, newt = do_tokenize(text2, form)
        
	f_po_freqdist = nltk.FreqDist(oldt)
	f_pn_freqdist = nltk.FreqDist(newt)

	chi_sq_dict = {}

	# make a union of old and new bigrams

	poset = set(f_po_freqdist.keys())
	pnset = set(f_pn_freqdist.keys())

	allbigrams = poset.union(pnset)

	for phrase in allbigrams:
	    chi_sq_dict[phrase] = do_chi_square(phrase, f_po_freqdist,
	    f_pn_freqdist)

	phrases=sorted(chi_sq_dict.items(), key=itemgetter(1))
	phrases.reverse()

	# now separate the OLD phrases from the NEW phrases:

	old_phrases = []
	new_phrases = []
	for (p,chisq) in phrases:
	    if (f_po_freqdist[p]>f_pn_freqdist[p]):
	        old_phrases.append((p, chisq))
	    else:
	        new_phrases.append((p,chisq))
	        
	print "DISTINGUISHING PHRASES FROM FIRST TEXT:"
	for o in range(0,10):
	    print ' '.join(old_phrases[o][0])
			
	print "\nDISTINGUISHING PHRASES FROM SECOND TEXT:"		
	for o in range(0,10):
	    print ' '.join(new_phrases[o][0])
	
	return old_phrases, new_phrases


