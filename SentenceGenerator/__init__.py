from random import randint


class SentenceGenerator:
    def __init__(self):
        self.array = []

    def add(self):
        print("Input a word:")
        self.array.append(input().strip().lower())

    def generateSentence(self):
        sentence_length = randint(1, 15)
        return [
            self.array[randint(0, len(self.array) - 1)] for _ in range(sentence_length)
        ]

    def show_sentence(self):
        print(" ".join(self.generateSentence()))
