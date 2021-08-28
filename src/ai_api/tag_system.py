from pymorphy2 import MorphAnalyzer

morph = MorphAnalyzer()


def add_target(words):
    new_words = []
    for word in words:
        parsed_word = morph.parse(word)[0]
        new_words.append(parsed_word.normal_form + '_' + parsed_word.tag.POS)
    return new_words

print(add_target(['работой']))
