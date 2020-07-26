# Pattern

# ****
# ***
# **
# *

def my_pythonic_way():
    for i in range(20, 0, -1):
        print(i * "*")


def usual_way():
    for i in range(1, 5):
        for j in range(1, 5):
            if j <= 5 - i:
                print("*", end='')
        print()


# my_pythonic_way()
usual_way()
