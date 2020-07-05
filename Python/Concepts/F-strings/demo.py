
# These are new way to format strings in Python 3.6 or above.

def check1():
    first_name = 'abc'
    last_name = 'pqr'

    sentence = 'My name is {} {}'.format(first_name, last_name)
    print(sentence)

    sentence = f'My name is {first_name} {last_name}'
    sentence = f'My name is {first_name.upper()} {last_name.upper()}'
    print(sentence)


def check2():
    person = {'name': 'ABC', 'age': 23}
    sentence = 'Name is {} and age is {}'.format(person['name'], person['age'])
    print(sentence)

    sentence = f"Name is {person['name']} and age is {person['age']}"
    print(sentence)


def check3():
    calculations = f"4 times 11 is qual to {4 * 11}"
    print(calculations)


def check4():
    for n in range(1, 11):
        sentence = f'The value of n is {n:02}'
        print(sentence)


def check5():
    pi = 3.14159265
    sentence = f"Pi is equal to {pi:.4f}"
    print(sentence)


def check6():
    from datetime import datetime

    d = datetime(1990, 1, 1)
    sentence = f'Date Mentioned -> {d: %B %d, %Y}'
    print(sentence)


# check1()
# check2()
# check3()
# check4()
# check5()
check6()
