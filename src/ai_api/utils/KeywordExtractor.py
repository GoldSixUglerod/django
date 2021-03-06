from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ssl
import nltk


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('stopwords')


class KeywordsExtractor:
    _initialized = False

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(KeywordsExtractor, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if not self._initialized:
            self._stop_words = nltk.corpus.stopwords.words('russian')
            self._n_gram_range = (1, 1)
            self._model = SentenceTransformer('DeepPavlov/rubert-base-cased-sentence')
            self._top_n = 5
            self._initialized = True

    def extract(self, text):
        # Extract candidate words/phrases
        count = CountVectorizer(
            ngram_range=self._n_gram_range, stop_words=self._stop_words
        ).fit([text])
        candidates = count.get_feature_names()
        doc_embedding = self._model.encode([text])
        candidate_embeddings = self._model.encode(candidates)
        distances = cosine_similarity(doc_embedding, candidate_embeddings)
        keywords = [
            candidates[index] for index in distances.argsort()[0][-self._top_n:]
        ]
        confidences = [
            distances[0][index] for index in distances.argsort()[0][-self._top_n:]
        ]

        return keywords, confidences
