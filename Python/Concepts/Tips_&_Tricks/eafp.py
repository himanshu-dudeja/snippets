# Easier to ask forgiveness than permission (EAFP)

def example1():
    # person = {'name': 'ABC', 'age': 24, 'job': 'Analyst'}
    person = {'name': 'ABC', 'age': 24}

    # LBYL (Non-pythonic) (Look before you lead)

    def lbyl():
        if 'name' in person and 'age' in person and 'job' in person:
            print(
                "I'm {name} and my age is {age} and work as {job}".format(**person))
        else:
            print("Missing some keys")

    # lbyl()

    def eafp():
        try:
            print(
                "I'm {name} and my age is {age} and work as {job}".format(**person))
        except KeyError as e:
            print(f"Missing {e} key")

    eafp()


def example2():
    my_list = [1, 2, 3, 4, 5]

    # Non-Pythonic
    if len(my_list) >= 6:
        print(my_list[5])
    else:
        print('Index does not exists')

    # Pythonic
    try:
        print(my_list[5])
    except IndexError as e:
        print(e)


def example3():
    import os
    my_file = '/tmp/test.txt'

    # Race Condition
    if os.access(my_file, os.R_OK):
        with open(my_file) as f:
            print(f.read())
    else:
        print('File cannot be accessed')

    # No Race condition
    try:
        f = open(my_file)
    except IOError as e:
        print(e)
    else:
        with f:
            print(f.read())


# example1()
# example2()
example3()
