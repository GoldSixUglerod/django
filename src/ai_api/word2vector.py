import zipfile
import gensim


with zipfile.ZipFile("model.zip", 'r') as archive:
    stream = archive.open('model.bin')
    model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)

