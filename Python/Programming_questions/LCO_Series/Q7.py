
# Question -
# The city bus system carries 1,200,000 people each day. How many people does the bus system carry each year?(1year = 365 days)
# Solve without using *, / operator, bitwise operator, or loop


def multiply(x, y):
    if y == 0:
        return 0
    if y > 0:
        return (x + multiply(x, y - 1))
    if y < 0:
        return -multiply(x, -y)


people_travel_daily = 1200000
days = 365
people_travel = multiply(people_travel_daily, days)
print(people_travel)
