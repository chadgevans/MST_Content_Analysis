import itertools as it
import re

def getNGrams(text,n=2,**args):
	hardStops = r"[^\d\w,'\"(-) ]"
	text = re.split(hardStops,text)
	
	text = filter(None,text)
	
	if 'stopwords' in args:
		swIter = it.repeat(
			args['stopwords'],len(text)
		)
		text=map(tokenize,text,swIter)
	else:
		text = map(tokenize,text)
	
	
	ngramCount = {} # I am extending Ngrams into counting them.  week 7, page 11
	for line in text:
		if len(line) >= n:
			for i in xrange(len(line)-n):
				ngram = line[ i:(i+n) ]
				ngram = tuple(ngram)
				if ngram in ngramCount:
					ngramCount[ngram] += 1
				else:
					ngramCount[ngram] = 1
	
	return(ngramCount)
	#There is one more page on multiple files


