
from collections import Counter


def Creating():
    # With sequence of items
    print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

    # with dictionary
    print(Counter({'A': 3, 'B': 5, 'C': 2}))

    # with keyword arguments
    print(Counter(A=3, B=5, C=2))

    # Create a list
    z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
    # Count distinct elements and print Counter object
    print(Counter(z))

    # More on how to print
    coun = Counter(['A', 'B', 'C', 'A', 'X', 'A', 'B'])
    print(coun)
    for item in coun.items():
        print(item)


Creating()


def updations():
    coun = Counter()
    print(coun)

    coun.update([1, 2, 3, 1, 2, 1, 1, 2])
    print(coun)

    coun.update([1, 2, 4])
    print(coun)


# updations()


def other_operations():
    c1 = Counter(A=4,  B=3, C=10)
    c2 = Counter(A=10, B=3, C=4)

    c1.subtract(c2)
    print(c1)


# other_operations()
