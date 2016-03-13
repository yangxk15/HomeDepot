# SnowballStemmer

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer('english')

def str_stemmer(s):
	return " ".join([stemmer.stem(word) for word in s.lower().split()])
