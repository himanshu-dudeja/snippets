def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


num = 5
if num < 0:
    print("No Negative numbers")
elif num == 0:
    print("Factorial is - 1")
else:
    print("Factorial is - {}".format(fact(num)))
