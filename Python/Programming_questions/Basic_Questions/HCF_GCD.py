# Program to calculate HCF

def hcf_method1(a, b):
    # a, b = input("Enter 2 numbers (separated by space) - ")
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            print(f"{i} is the HCF")
            break


hcf_method1(5, 3)


def hcfnaive(a, b):
    if(b == 0):
        return a
    else:
        return hcfnaive(b, a % b)


print(hcfnaive(48, 60))


# method to compute gcd ( Euclidean algo )
def computeGCD(x, y):

    while(y):
        x, y = y, x % y
    return x


print(computeGCD(60, 48))
