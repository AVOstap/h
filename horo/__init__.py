import random


class SentenceGenerator:
    def __init__(self, words_chain: dict, start_words: list):
        self.words_chain = words_chain
        self.start_words = start_words

    def generate_sentence(self):
        text = []
        first_word = random.choice(self.start_words)
        text.append(first_word.title())
        second_word = random.choice(self.words_chain[first_word])
        text.append(second_word)

        while True:
            try:
                third_word = random.choice(self.words_chain[first_word + " " + second_word])
            except KeyError:
                break
            text.append(third_word)
            first_word, second_word = second_word, third_word
        return " ".join(text)

    def generate_text(self, max_sentence_number=3):
        text = ''
        number_sentence = random.choice(range(max_sentence_number))
        for i in range(number_sentence + 1):
            text += " " + self.generate_sentence()
        return text


def get_sentence_generator(file_name: str)-> "SentenceGenerator":
    with open(file_name, encoding="utf8") as file:
        text = file.read()

    punctuation = r'"#$%&\'-–()*,+/:<=>@[\\]^_`{|}~﻿'
    trans = str.maketrans(punctuation, " " * len(punctuation))
    text = text.split()
    all_start_words = []
    words_chain = {}

    pw, ppw = "", ""
    for word in text:
        word = word.translate(trans).strip()
        if not word:
            continue
        if not pw:
            word = word.lower()
            if not words_chain.get(word):
                words_chain[word] = []
            all_start_words.append(word)
        if ppw:
            key = ppw + " " + pw
            if not words_chain.get(key):
                words_chain[key] = []
            words_chain[key].append(word)
        else:
            if pw:
                words_chain[pw].append(word)
        if word[-1:] in ".!?;":
            pw, ppw = "", ""
        else:
            ppw, pw = pw, word

    return SentenceGenerator(words_chain, all_start_words)

if __name__ == '__main__':
    seq = get_sentence_generator('../h.txt')
    print(seq.generate_text(3))
