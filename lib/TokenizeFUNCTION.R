# Chad Evans
# Content Analysis
rm(list=ls())
library(hash)
#No Sink
setwd("/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/Tokenizing")
f<-file('/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/Tokenizing','r')
lines<-readLines("/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/Tokenizing/Roseli.txt",encoding='latin1')

s= "I am a string"

# tokenizing
tokenize=function(text){
	text=tolower(text)
	
	pat="[^\\d\\w']+"# ^ within brackets mean something new.  It means "not" in this form
	text=strsplit(text,pat,perl=TRUE)
	text=text[[1]] # hack
# then put: strsplit(s,'[ai]')
# [[1]]
return(text)
}

