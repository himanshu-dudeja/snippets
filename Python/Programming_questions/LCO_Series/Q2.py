# Question
# Print Double sided stair-case * pattern

#             * *
#             * *
#           * * * *
#           * * * *
#         * * * * * *
#         * * * * * *
#       * * * * * * * *
#       * * * * * * * *
#     * * * * * * * * * *
#     * * * * * * * * * *

def exact_pattern(n):
    n = int(n / 2)
    for i in range(1, n + 1):
        print((n - i) * " " + (i * 2) * "*" + (n - i) * " ")
        print((n - i) * " " + (i * 2) * "*" + (n - i) * " ")


def proper_way(n):
    for i in range(1, n + 1):
        k = i if(i % 2 == 0) else i + 1
        for _ in range(n, k, -1):
            print(" ", end='')
        for j in range(k):
            print("* ", end='')
        print()


# exact_pattern(10)
proper_way(10)
