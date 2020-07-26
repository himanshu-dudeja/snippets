# Input : 6
# Output :
#
# * * * * * *
# * * * * * *
# * * * *
# * * * *
# * *
# * *

def pattern(n):
    for i in range(n, 0, -1):
        k = i if (i % 2 == 0) else i + 1
        for j in range(0, k):
            print("* ", end='')
        print()


pattern(6)
