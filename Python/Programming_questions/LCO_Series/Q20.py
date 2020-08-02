"""
Find the square of a number without using multiplication or division operator.
"""

# First method
print(9**2)

# Second method
import math
print(math.pow(9, 2))


# Third method
def find_square(n):
    sum = 0
    for i in range(n):
        sum = sum + n
    print(sum)


find_square(9)
