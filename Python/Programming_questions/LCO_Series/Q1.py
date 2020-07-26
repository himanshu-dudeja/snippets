# Question -
"""There was a Teacher in a small town who loves coding and he wants
 to create a program which prints out the whole multiplication table
 of an entered number for his students."""


def tabel(number):
    for i in range(1, 11):
        print(f"{number} * {i} = {number*i}")


tabel(5)
