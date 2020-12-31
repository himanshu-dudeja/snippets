def reverse_way1(string):
    return string[::-1]


def reverse_way2(string):
    str1 = ""
    for i in string:
        str1 = i + str1
    return str1


def reverse_way3(string):
    str1 = ""
    for i in range(len(string) -1, -1, -1):
        str1 = str1 + string[i]
    return str1


print(reverse_way1("Hello World"))
print(reverse_way2("Hello World"))
print(reverse_way3("Hello World"))

