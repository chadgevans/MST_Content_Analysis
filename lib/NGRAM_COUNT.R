# Chad Evans
# Content Analysis
# Final Project
rm(list=ls())
library(hash)
#No Sink
setwd("/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/N-grams")
f<-file('/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/N-grams','r')
lines<-readLines("/Users/chadgevans/Desktop/Content Analysis/ComputerFiles/N-grams/Roseli.txt",encoding='latin1')


s= "I am a string and I like to eat icecream and the end of the world is coming if my ice cream cone is not chocolate.  I hope i don't die.  I want to go to the park and play with the squirrels.  Dogs are my friends because they play with tennis balls.  Pete Sampras also plays with tennis balls, but he is not my friend."


tokenize=function(text, stopwords=c()){
	text=tolower(text)
	pat="[^\\d\\w']+"
	text=strsplit(text, pat, perl=TRUE)
	text=text[[1]]
	
	sw=text%in% c(stopwords, "")
	text=text[!sw]
	
	return(text)
}
	
	
getNGrams=function(text,n=2){
	hardStops="[^\\d\\w,'\"(-) ]"
	text=strsplit(text, hardStops, perl=T) [[1]]
	
text2=text[text != '']
t_text=lapply(text2, tokenize)
ngramCount<-hash()
for(line in t_text){
	if(length(line)>=n){
		for(i in seq(length(line)-n+1) ){
		ngram<- line[i:(i+n-1)]
		ngram<-paste(ngram,collapse=' ')
		if( has.key(ngram,ngramCount) ){
			ngramCount[[ngram]]<-
				ngramCount[[ngram]]+ 1
			}else{
				ngramCount[[ngram]]<- 1
				}
			}
		}
	}
return(ngramCount)
}
#getNGrams(s)
#getNGrams(s,n=13) now we enter n=to some number and find the strings
