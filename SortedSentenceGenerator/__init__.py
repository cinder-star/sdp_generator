from SentenceGenerator import SentenceGenerator


class SortedSentenceGenerator(SentenceGenerator):
    def show_sentence(self):
        sentence = self.generateSentence()
        sentence.sort()
        print(" ".join(sentence))
