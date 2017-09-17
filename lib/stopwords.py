import nltk
text=open('/Users/chadgevans/Desktop/PythonDocs/MSTCorpus/1.txt','r')
lines<-readLines("/Users/chadgevans/Desktop/PythonDocs/MSTCorpus/1.txt",encoding='latin1')
text=nltk.word_tokenize(lines)
nltk.pos_tag(text) # long time and poor results

stopwords=open('/Users/chadgevans/nltk_data/corpora/stopwords/portuguese','r')

for x in text:
  if x in stopwords:
    delete x from text