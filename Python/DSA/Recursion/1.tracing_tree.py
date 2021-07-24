def func(n):
    if n > 0:
        print("Val is - {}".format(n))
        func(n-1)
        # print("Val is - {}".format(n))


func(3)
