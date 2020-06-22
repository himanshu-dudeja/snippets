
class Sentence:
    def __init__(self, _string):
        self.string = _string.split()
        self.start = 0
        self.end = len(self.string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        data = self.string[self.start]
        self.start += 1
        return data


# my_sentence = Sentence('This is a test')

# for word in my_sentence:
#     print(word)

# print(next(my_sentence))
# print(next(my_sentence))


# Same example with generator ->

def gen_example(string):
    for _str in string.split():
        yield _str


_it = gen_example('This is a test')

for __it in _it:
    print(__it)

# print(next(_it))
# print(next(_it))
# print(next(_it))
# print(next(_it))
