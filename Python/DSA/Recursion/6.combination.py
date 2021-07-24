def fact(n):
    val = 1
    for i in range(2, n+1):
        val = i * val
    return val


def combination(n, r):
    return int(fact(n) / (fact(r) * fact(n-r)))


print(combination(5, 3))
