
"""
LEGB
Local, Enclosing, Global, Built-in
"""

x = 'global x'

# Concept for Local and global variable
def local_and_global_scope():

    def test():
        y = 'local y'
        print(y)
        print(x)

    test()

    # Check for the x param inside and outside the func.
    def test1():
        x = 'local x'
        print(x)

    print(x)
    test1()

    # Changing the global variable.

    def test2():
        global x
        x = 'local x'
        print(x)

    print(x)
    test2()
    print(x)


def built_in_scope():
    # Check the builtins
    import builtins
    print(dir(builtins))

    # Creating a similar function as min
    m = min([23, 5, 4, 1, 3])
    print(m)

    def min(x):
        print(x)

    min([23, 5, 4, 1, 3])


def enclosing_scope():

    def outer():
        x = 'outer x'

        def inner():
            # x = 'inner x'
            print(x)
        inner()
        print(x)
    outer()

def nonlocal_statement():

    def outer():
        x = 'outer x'

        def inner():
            nonlocal x
            x = 'inner x'
            print(x)
        print(x)
        inner()
        print(x)
    outer()


# local_and_global_scope()
# built_in_scope()
# enclosing_scope()
# nonlocal_statement()
