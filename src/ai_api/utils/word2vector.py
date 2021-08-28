import zipfile
import gensim
from pymorphy2 import MorphAnalyzer


morph = MorphAnalyzer()


def add_target(words):
    new_words = []
    for word in words:
        parsed_word = morph.parse(word)[0]
        new_words.append(str(parsed_word.normal_form) + '_' + str(parsed_word.tag.POS))
    return new_words


def download_model():
    with zipfile.ZipFile('model.zip', 'r') as archive:
        stream = archive.open('model.bin')
        model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
    return model


def vectorize_word(word, model):
    word_with_tag = add_target(word)
    return model[[word_with_tag]]
