import itertools


def _count():
    # By Default if we don't pass any args then this will start from 0 and will inc. by 1 in each iteration
    counter = itertools.count()
    counter = itertools.count(start=20, step=5)
    counter = itertools.count(start=20, step=-5.5)
    print(next(counter))
    print(next(counter))

    data = [100, 200, 300, 400]
    updated_data = list(zip(itertools.count(), data))
    print(updated_data)


def _zip_longest():
    # This will pair to the longest range available and for remaning it will be NONE
    data = [100, 200, 300, 400]
    updated_data = list(itertools.zip_longest(range(10), data))
    print(updated_data)


def cycle():
    counter = itertools.cycle([1, 2, 3])
    counter = itertools.cycle(('on', 'off'))
    for _ in range(10):
        print(next(counter))


def repeat():
    counter = itertools.repeat(2)
    counter = itertools.repeat(2, times=3)
    for _ in range(2):
        print(next(counter))

    squares = map(pow, range(10), itertools.repeat(2))
    print(list(squares))


def starmap():
    # This startmap takes input as list of tuples
    squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
    print(list(squares))


def combinations():
    # Different ways by which we can group certain number of items where ORDER DOES NOT MATTER.
    letters = ['a', 'b', 'c', 'd']

    results = itertools.combinations(letters, 2)
    for item in results:
        print(item)


def permutations():
    # Different ways by which we can group certain number of items where ORDER DOES MATTER.
    letters = ['a', 'b', 'c', 'd']
    results = itertools.permutations(letters, 2)
    for item in results:
        print(item)


def product():
    # In case we want to repeat the values (cartesian product)
    numbers = [0, 1, 2, 3]
    results = itertools.product(numbers, repeat=2)
    for item in results:
        print(item)


def combinations_with_replacement():
    numbers = [0, 1, 2, 3]
    results = itertools.combinations_with_replacement(numbers, 2)
    for item in results:
        print(item)


def chain():
    # Helps to chain the iterables
    letters = ['a', 'b', 'c', 'd']
    numbers = [1, 2, 3, 4]
    names = ['ABC', 'CDC']
    combined = itertools.chain(letters, numbers, names)
    for item in combined:
        print(item)


def islice():
    # Helps perform slicing over an iterator
    result = itertools.islice(range(10), 5)
    result = itertools.islice(range(10), 1, 6)
    result = itertools.islice(range(10), 1, 6, 2)
    for item in result:
        print(item)


def compress():
    # This will check the correponding values are True, False (Shortest list)
    letters = ['a', 'b', 'c', 'd', 'e']
    selectors = [True, True, False, True]
    result = itertools.compress(letters, selectors)
    for item in result:
        print(item)


def filter_related():
    # The similar concpet is there for in-built filter function.
    print("Filter Function")

    def lt_2(n):
        if n < 2:
            return True
        return False

    numbers = [0, 1, 2, 3, 4]
    result = filter(lt_2, numbers)
    for item in result:
        print(item)

    # Filter False Function -
    print("Filter False Function")
    result = itertools.filterfalse(lt_2, numbers)
    for item in result:
        print(item)

    # Drop While Function
    # This will drop values from an iterable untill one of the values return True
    print("Drop While Function")
    numbers = [0, 1, 2, 3, 2, 1]
    result = itertools.dropwhile(lt_2, numbers)
    for item in result:
        print(item)

    # Take While function
    # This will grab the values which are true, and as it hits the value that does'nt return True, Then it retuns the values at that point.
    print("Take While function")
    numbers = [0, 1, 2, 3, 2, 1]
    result = itertools.takewhile(lt_2, numbers)
    for item in result:
        print(item)


def accumulate():
    import operator
    numbers = [1, 2, 3, 4, 2, 1]
    # This will add the nums
    result = itertools.accumulate(numbers)
    # We can also do other mul etc..
    result = itertools.accumulate(numbers, operator.mul)
    for item in result:
        print(item)

def group_by():

    # IMP NOTE : This requires the Data to be sorted.
    # Here the data is alreday sorted on the basis of state i.e NY is first 2 and CO is the other one and So on...
    # This is diff from SQL version as this requires sorting.

    people = [
        {
            'name': 'John Doe',
            'city': 'Gotham',
            'state': 'NY'
        },
        {
            'name': 'Jane Doe',
            'city': 'Kings Landing',
            'state': 'NY'
        },
        {
            'name': 'Corey Schafer',
            'city': 'Boulder',
            'state': 'CO'
        },
        {
            'name': 'Al Einstein',
            'city': 'Denver',
            'state': 'CO'
        },
        {
            'name': 'John Henry',
            'city': 'Hinton',
            'state': 'WV'
        },
        {
            'name': 'Randy Moss',
            'city': 'Rand',
            'state': 'WV'
        },
        {
            'name': 'Nicole K',
            'city': 'Asheville',
            'state': 'NC'
        },
        {
            'name': 'Jim Doe',
            'city': 'Charlotte',
            'state': 'NC'
        },
        {
            'name': 'Jane Taylor',
            'city': 'Faketown',
            'state': 'NC'
        }
    ]

    def get_state(person):
        return person['state']

    person_group = itertools.groupby(people, get_state)
    for key, group in person_group:
        print(key)
        for person in group:
            print(person)
        print()


def tee():
    # This will help in the replication of iterators.
    l1 = [1, 2, 3, 4]
    l1_iter = iter(l1)

    copy1, copy2 = itertools.tee(l1_iter)

    print("Print via next method")
    print(next(l1_iter))
    print(next(l1_iter))
    print(next(l1_iter))

    print("Print via copy1")
    for i in copy1:
        print(i)

    print("Print via copy2")
    for j in copy2:
        print(j)


if __name__ == '__main__':
    # _count()
    # _zip_longest()
    # cycle()
    # repeat()
    # starmap()
    # combinations()
    # permutations()
    # product()
    # combinations_with_replacement()
    # chain()
    # islice()
    # compress()
    # filter_related()
    # accumulate()
    # group_by()
    tee()
