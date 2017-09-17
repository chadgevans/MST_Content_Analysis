import nltk
from nltk.corpus import movie_reviews
import random
from nltk.corpus import brown

suffix_fdist = nltk.FreqDist()
for word in brown.words():
	word = word.lower()
	suffix_fdist.inc(word[-1:])
	suffix_fdist.inc(word[-2:])
	suffix_fdist.inc(word[-3:])
	
common_suffixes = suffix_fdist.keys()[:100]
print common_suffixes

def pos_features(word):
	features = {}
	for suffix in common_suffixes:
		features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
	return features

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]

size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]

classifier = nltk.DecisionTreeClassifier.train(train_set)
nltk.classify.accuracy(classifier, test_set)

classifier.classify(pos_features('cats'))
# it froze the computer at this point

