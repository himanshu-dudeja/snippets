"""
A sells lemonade at 5 cents, sold k no. of glasses
B sells lemonade at 7 cents, sold r no. of glasses
Who made more money and by what amount?
"""

a = 5
b = 7
k = int(input("Please enter no. of glasses sold by Kara - "))
r = int(input("Please enter no. of glasses sold by Rani - "))
ka = k * a
print("kara_amount - ", ka)
ra = r * b
print("rani_amount - ", ra)
print("Kara made more money") if ka > ra else print(
    "Both made same amount") if ka == ra else print("Rani made more money")
print("Amount diff - ", abs(k * a - r * b))
