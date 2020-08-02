"""
Lengths = 12,13,8,10,17
Find the largest without using conditional statemnets and the loop
"""


def find_largest(arr):
    return sorted(arr)[-1]


print(find_largest([12, 13, 8, 10, 17]))
