import zipfile
import gensim


def download_model():
    with zipfile.ZipFile('/model.zip', 'r') as archive:
        stream = archive.open('model.bin')
        model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
    return model


model = download_model()
print(model['работа_NOUN'])
