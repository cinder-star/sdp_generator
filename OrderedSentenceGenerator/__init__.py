from SentenceGenerator import SentenceGenerator


class OrderedSentenceGenerator(SentenceGenerator):
    def add(self):
        print("Input a word:")
        self.array.append(input().strip().upper()[::-1])

    def generateSentence(self):
        return self.array
