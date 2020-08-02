"""
Program to get the sum of n numbers.
sum of 123 is 6
"""


def sum_of_num(num):
    l = []
    sum = 0
    while int(num) != 0:
        l.append(num % 10)
        num = num // 10
    for i in l:
        sum = sum + i
    print(sum)


# sum_of_num(int(123))

def easy_method(mylist):
    sum = 0
    for i in str(mylist):
        sum = sum + int(i)
    print(sum)


easy_method(int(123))
