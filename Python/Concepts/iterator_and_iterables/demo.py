# Iterable ->
# A list is iterable because it can be looped over.
# If something is iterable it has to have a dunder method called '__iter__'

def iterables_demo():
    nums = [1, 2, 3]
    # for num in nums:
    #     print(num)
    print(dir(nums))
    print(next(nums))  # This will give an error

# Iterator ->
# An object with a state so that it remembers where it is during iteration.
# Iterator can only go forward, no going backwards, no reseting it or making a copy of it. Only we can go forward by calling next()


def iterator_demo():
    nums = [1, 2, 3]
    # i_nums = nums.__iter__()
    i_nums = iter(nums)
    print(i_nums)
    print(dir(i_nums))
    print(next(i_nums))
    print(next(i_nums))
    print(next(i_nums))


def back_story_of_for_loop():
    nums = [1, 2, 3]
    i_nums = iter(nums)
    while True:
        try:
            item = next(i_nums)
            print(item)
        except StopIteration:
            break


def own_range():
    class MyRange:
        def __init__(self, start, end):
            self.value = start
            self.end = end

        def __iter__(self):
            return self

        def __next__(self):
            if self.value >= self.end:
                raise StopIteration
            current = self.value
            self.value += 1
            return current

    nums = MyRange(1, 5)
    print(dir(nums))
    # for num in nums:
    #     print(num)
    print(next(nums))
    print(next(nums))


# Generator function will create the __next__ and __iter__ dunder methods by itself.
def generator_range():
    def my_range(start, end):
        current = start
        while current < end:
            yield current
            current += 1

    nums = my_range(1, 10)

    print(dir(nums))

    print(next(nums))
    print(next(nums))
    print(next(nums))

    print("NEXT DONE")

    for num in nums:
        print(num)


if __name__ == '__main__':
    # iterables_demo()
    # iterator_demo()
    # back_story_of_for_loop()
    # own_range()
    # generator_range()
