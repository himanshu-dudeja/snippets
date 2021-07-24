def way1(n):
    if n > 0:
        print("Val is - {}".format(n))
        way1(n-1)
        way1(n-1)


def way2(n):
    if n > 0:
        way2(n-1)
        way2(n-1)
        print("Val is - {}".format(n))


def way3(n):
    if n > 0:
        way3(n-1)
        print("Val is - {}".format(n))
        way3(n-1)


way3(3)
