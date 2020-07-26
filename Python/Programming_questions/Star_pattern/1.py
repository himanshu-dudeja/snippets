# Pattern

# *
# **
# ***
# ****

def my_pythonic_way(n):
    for i in range(1, n):
        print(i * "*")


def another_way():
    for i in range(1, 5):
        for j in range(1, 5):
            if j <= i:
                print("*", end=' ')
            else:
                print(end=' ')
        print()


my_pythonic_way(5)
another_way()
