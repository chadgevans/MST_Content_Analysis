import re

def tokenize(text, stopwords=[]):
	text = text.lower()
	
	pat = r"[\d\w']+"
	text = re.findall(pat,text)
	
	res = []
	for w in text:
		if w not in stopwords:
			res += [w]
			
	return(res)

#This function works