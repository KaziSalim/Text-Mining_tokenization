# Tokenization =ngram

# using custom function(n gram)

import re

def n_gram_custom(input,n):
    tokens = re.sub(r'([^\s\w]|_)+', ' ',input).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_custom('Virat Kohli is a great player', 3)        


# using nltk library(Natural language toolkit)

from nltk import word_tokenize

word = word_tokenize("Virat Kohli is a great player")
print(word)


from nltk import ngrams

list(ngrams("Virat Kohli is a great player.".split(),1))

list(ngrams("Virat Kohli is a great player.".split(),2))

list(ngrams("Virat Kohli is a great player.".split(),3))


# using textblob

from textblob import TextBlob

blob = TextBlob("Virat Kohli is a great player")

blob.ngrams(n=2)


blob.ngrams(n=3)
