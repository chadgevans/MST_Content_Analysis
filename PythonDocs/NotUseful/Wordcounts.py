import re

f= file('/Users/chadgevans/Desktop/PythonDocs/Genesis.txt','r')
lines = f.readlines()

wordcounts={}
for line in lines:
	line = line.rstrip()
	line_spl=line.split(' ')
	# is the first word an integer value??
	if re.match("\d",line_spl[0]):
		line_spl=line_spl[1:len(line_spl)]
	for word in line_spl:
		if wordcounts.has_key(word):
			wordcounts[word] += 1
		else:
			wordcounts[word] = 1
print wordcounts