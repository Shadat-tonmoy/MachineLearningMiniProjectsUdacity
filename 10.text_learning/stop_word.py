from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
sw = stopwords.words("english")
print len(sw)
snowballStemmer = SnowballStemmer("english")
words = ['responsiveness','response','responsive','unresponsive','unresponsiveness']
for word in words:
    print word," Stemmed to ",snowballStemmer.stem(word)

