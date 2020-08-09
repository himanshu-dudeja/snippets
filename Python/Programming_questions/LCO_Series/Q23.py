"""
Convert int val into binary
"""


def convert_into_binary(val):
    print(bin(val)[2:])


convert_into_binary(int(9))


def binary_coversion_code(val):
    l = []
    while val != 1:
        l.append(str(val % 2))
        val = val // 2
    l.append(str(1))
    # reverse the list
    print(''.join(l[::-1]))


binary_coversion_code(9)
