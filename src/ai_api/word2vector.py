import zipfile
import gensim


def download_model():
    with zipfile.ZipFile('/Users/danildavydyan/PycharmProjects/djangoApi/model.zip', 'r') as archive:
        stream = archive.open('model.bin')
        model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
    return model
