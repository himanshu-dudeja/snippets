def f1(n):
    my_list = [0, 1]
    for i in range(2, n):
        my_list.append(my_list[i-1] + my_list[i-2])
    return my_list


def f2(n):
    if n <= 1:
        return n
    else:
        return f2(n-1) + f2(n-2)


print(f1(10))
for i in range(10):
    print(f2(i), end=" ")
