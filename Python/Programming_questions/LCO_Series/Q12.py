"""
Red blood corpuscles in 1 cubic millimeter = 5000000
White blood corpuscles in 1 cubic millimeter = 8000

What is the ratio of white to red ?
Aspect ratio should be as an int value
"""

RBC = 5000000
WBC = 8000

# Calculate GCD to get the factor


def calculate_gcd(a, b):
    if b == 0:
        return a
    else:
        return calculate_gcd(b, a % b)


factor = calculate_gcd(RBC, WBC)
print(f"GCD is - {factor}")

white = WBC // factor
red = RBC // factor
print(f"Ratio of white:red is - {white}:{red}")
