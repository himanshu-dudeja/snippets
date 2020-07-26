# Pattern

# *******
# *** ***
# **   **
# *     *

def my_way():
    for i in range(1, 5):
        for j in range(1, 8):
            if j >= 6 - i and j <= i + 2:
                print(" ", end='')
            else:
                print("*", end='')
        print()


def usual_way():
    for i in range(1, 5):
        for j in range(1, 8):
            if j <= 5 - i or j >= 3 + i:
                print("*", end='')
            else:
                print(" ", end='')
        print()


my_way()
# usual_way()
