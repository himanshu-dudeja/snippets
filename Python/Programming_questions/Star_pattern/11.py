# Input : 6
# Output :
#
# * * * * * *
# * * * * * *
#   * * * *
#   * * * *
#     * *
#     * *

def pattern(n):
    for i in range(n, 0, -1):
        k = i if (i % 2 == 0) else i + 1
        for _ in range(k, n):
            print(" ", end='')
        for j in range(k):
            print("* ", end='')
        print()


pattern(6)
