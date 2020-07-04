
def using_ternary_operators():
    condition = True

    # old way
    if condition:
        x = 1
    else:
        x = 0
    print(x)

    # New way
    x = 1 if condition else 0
    print(x)


def dealing_with_large_numbers():
    # Old Way
    num1 = 100000000
    num2 = 1000000
    total = num1 + num2
    print(total)

    # New Way
    num1 = 100_000_000
    num2 = 1_000_000
    total = num1 + num2
    print(f"{total:,}")


def using_context_managers():
    # Old Way
    f = open('test.txt', 'r')
    file_contents = f.read()
    f.close()

    # New Way
    with open('test.txt', 'r') as f:
        file_contents = f.read()


def using_enumerate():
    # Old Way
    names = ['aa', 'bb', 'cc', 'dd']
    index = 0
    for name in names:
        print(index, name)
        index += 1

    # New Way
    names = ['aa', 'bb', 'cc', 'dd']
    for index, name in enumerate(names, start=1):
        print(index, name)


def using_zip_function():
    names_cap = ['A', 'B', 'C', 'D']
    names_sma = ['a', 'b', 'c', 'd']
    more_list = ['1', '2', '3', '4']

    # Old Way
    for index, name_cap in enumerate(names_cap):
        name_sma = names_sma[index]
        print(f"{name_cap} is {name_sma}")

    # New way
    for name_cap, name_sma, more in zip(names_cap, names_sma, more_list):
        print(f"{name_cap} is {name_sma} and {more}")


def unpacking_examples():
    items = (1, 2)
    print(items)

    a, b = (1, 2)
    print(a)
    print(b)

    # Anytime we need to ignore any variable in python we can use _
    a, _ = (1, 2)
    print(a)

    a, b, *c = (1, 2, 3, 4, 5)
    print(a, b, c)

    a, b, *c, d = (1, 2, 3, 4, 5)
    print(a, b, c, d)


def creating_objects_dynamically():
    class Person():
        pass
    person = Person()

    # # Ususal Way
    # person.first = "AAA"
    # person.last = "BBB"
    # print(person.first, person.last)

    # # Via Variable
    # setattr(person, 'first', 'AAA')
    # print(person.first)
    # last_key = 'last'
    # last_value = 'BBB'
    # setattr(person, last_key, last_value)
    # print(person.last)

    # # Via a dict
    person_info = {'first': 'AAA', 'last': 'BBB'}
    for k, v in person_info.items():
        setattr(person, k, v)
    for key in person_info.keys():
        print(getattr(person, key))


def input_password():
    # wrong way
    usename = input('Username: ')
    password = input('Password: ')
    print('Logging In...')

    # Correct way
    from getpass import getpass
    usename = input('Username: ')
    password = getpass('Password: ')
    print('Logging In...')

def using_m_option_in_python_terminal():
    '''
    >>example command - (starting the debug_mail server)
    >>python -m smtpd -c DebuggingServer -n localhost:1025
    >>Running the module that we specify after -m
    eg. smtpd and everything after that are the
    args of that.
    >>Why we are not running it directly because these script
    does'nt exists in the current dir. (this -m wiill search
    for sys.path for the respective module)
    '''


if __name__ == '__main__':
    # using_ternary_operators()
    # dealing_with_large_numbers()
    # using_context_managers()
    # using_enumerate()
    # using_zip_function()
    # unpacking_examples()
    # creating_objects_dynamically()
    # input_password()
