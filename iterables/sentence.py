class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.current_index = 0

    @property
    def words(self):
        return self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= len(self.words):
            raise StopIteration
        index = self.current_index
        self.current_index += 1
        return self.words[index]


def sentence(text):
    for word in text.split():
        yield word


# my_s = Sentence("This is a test")
my_s = sentence("This is a test")
for k in my_s:
    print(k)
