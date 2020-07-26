#  Input : 6

#  Output :
#  * *
#  * *
#  * * * *
#  * * * *
#  * * * * * *
#  * * * * * *

def pattern(n):
    for i in range(1, n + 1):
        k = i + 1 if (i % 2 != 0) else i
        for j in range(0, k):
            print("* ", end='')
            # if j == k - 1:
            #     print("* ")
            # else:
            #     print("* ", end='')
        print()


pattern(6)
