#  Input : 6
#  Output :
#      * *
#      * *
#    * * * *
#    * * * *
#  * * * * * *
#  * * * * * *


def pattern(n):
    for i in range(1, n + 1):
        k = i if(i % 2 == 0) else i + 1
        for g in range(n, k, -1):
            print(" ", end='')
        for j in range(0, k):
            print("* ", end='')
        print()


pattern(6)
