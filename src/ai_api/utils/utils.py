import ssl

import nltk
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from adminpage.loader import model


def vectorize_words(words_array):
    vectorized = []
    for word in words_array:
        vectorized_word = vectorize_word(word, model)
        vectorized.append(vectorized_word)
    return vectorized
