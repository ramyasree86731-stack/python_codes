#NLP codes


#Tokenisation


import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt_tab")
text = "hello hi how are you charan sathwik?"
tokens = word_tokenize(text)
print(tokens)


#stop words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
text = "this is a sample code written by abirami"
words = words_tokenize(text)
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("original:",text)
print("filtered:"," ".join(filtered_words))

#stemming

from nltk.stem import Porterstemmer
stemmer = Porterstemmer()
words = ["running","runner","eassily","fairiy"]
stemmed_words = [stemmer.stem(word)for word in words]
print("stemmed words:",stemmed_words)


#lemmatisation

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
words = ["running","runner","eassily","fairiy"]
lemmatized_words = [lemmatizer.lemmatize(word,pos=wordnet.VERB) for word in word]
print("lemmatized_words:",lemmatized_words)

#parts of speech tagging

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download("punkt")
nltk.download("averaaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
sentence = "The quick brown fox jumps over to the lazy dog."
tokens=word_tokenize(sentence)
tagged = pos_tag(tokens)
print(tagged)
"""

#syntax and parsing
"""
exp = "5+3*3"
result = eval(exp)
print(result)
"""

#LOWERCASING
"""
text = "HelloWorld"
lower= text.lower()
print(lower)
"""

#REMOVE SPECIAL CHARACTERS
"""
import string
def remove(text):
    return re.sub(r'[^A-Za-z0-9\s]',"",text)
i="helloo#@$!!! world!!"
c=remove(I)
print(C)
"""

#REMOVE PUNCTUATION
"""
import string
def remove_punctuation(text):
return text.translate(str.maketrans('', '', string.punctuation))
# Example usage
text = "Hello, world! Let's remove punctuation."
clean_text = remove_punctuation(text)
print(clean)
"""

#BAG OF WORDS
"""
from sklearn.feature_extraction.text import CountVectorizer
# Sample documents
documents = [
"I love programming in Python",
"Python is great for data science",
"I love learning new programming languages"
]
# Create the Bag of Words model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
# Get feature names and transformed data
feature_names = vectorizer.get_feature_names_out()
print("Feature Names:", feature_names)
print("Bag of Words Model:\n", X.toarray())
"""

def n_grams(text, n):
words = text.split()
return [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
# Example usage
text = "I love programming in Python"
n = 2
print(n_grams(text, n))









