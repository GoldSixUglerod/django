from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()


def add_target(words):
    return [word + "_" + morph.parse(word[0].tag.POS) for word in words]
