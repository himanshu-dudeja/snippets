# Difference b/w == and is operator?

# "==" checks for equality
# "is" checks for identity

def check_1():
    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 3, 4]
    if l1 == l2:
        print(True)
    else:
        print(False)
    print(id(l1))
    print(id(l2))


def check_2():
    l1 = [1, 2, 3, 4]
    l2 = [1, 2, 3, 4]
    if l1 is l2:
        print(True)
    else:
        print(False)
    print(id(l1))
    print(id(l2))


def check_3():
    l1 = [1, 2, 3, 4]
    l2 = l1
    if l1 is l2:
        print(True)
    else:
        print(False)
    print(id(l1))
    print(id(l2))


if __name__ == '__main__':
    check_1()
    check_2()
    check_3()
