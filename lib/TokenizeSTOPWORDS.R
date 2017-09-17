# Chad Evans
# Content Analysis
rm(list=ls())
library(hash)
#No Sink
setwd("/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/Tokenizing")
f<-file('/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/Tokenizing','r')
lines<-readLines("/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/Tokenizing/Roseli.txt",encoding='latin1')

s= "I am a string"

tokenize=function(text, stopwords=c()){          # this is where the stop words part is
	text=tolower(text)
	
	pat="[^\\d\\w']+"                        # ^ means "not" in this case
	text=strsplit(text,pat,perl=TRUE)
	text=text[[1]]                       # Peter's hack

# then put: strsplit(s,'[ai]')
# [[1]]

sw=text %in% stopwords
text=text[!sw]

return(text)
}

# Commands in the R Console to make it work
#x=1:5
#x
#st=c('b', 'dee')
# x %in% st
# tokenize(s, c('a', 'hi', 'b')) 3/9 it appears that this is where stopwords are put.  Not in the function.