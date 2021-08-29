from sentence_transformers import SentenceTransformer
import zipfile
import gensim
from pymorphy2 import MorphAnalyzer

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


morph = MorphAnalyzer()
w2v_model = download_model()
extracted = ['пожар', "отчет", "код"]
employees = ['пожарник', 'бухгалтер', 'программист']
employees_target = [tg.replace("ё", "е") for tg in add_target(employees)]
extracted_target = [tg.replace("ё", "е") for tg in add_target(extracted)]
empls = {}
for empl in employees_target:
    summ = 0
    for extr in extracted_target:
        sim = 0
        try:
            sim = w2v_model.similarity(empl, extr)
        except KeyError:
            pass
        summ += sim
        print(empl, extr, sim)
    empls[empl] = summ

max(empls, key=empls.get)
