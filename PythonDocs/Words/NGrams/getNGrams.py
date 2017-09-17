import re
import itertools as it


def getNGrams(text,n=2):
	hardStops = r"[^\d\w,'\"(-) ]"
	text = re.split(hardStops,text)
	
	text = filter(None,text)
	
	text=map(tokenize,text)
	
	return(text)
	
	#Not working