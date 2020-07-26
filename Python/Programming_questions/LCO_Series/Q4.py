# Question -
# Jack bought 400 hotdogs for school picnic.
# If they were contained in package of 8 hotdogs. how many total packages he had to buy?
# Python program without / or % operator.

def with_operators():
    total_hotdogs = 400
    bundel = 8
    no_of_bundels = total_hotdogs / bundel
    print(no_of_bundels)


def without_operators():
    total_hotdogs = 400
    bundel = 8
    count = 0
    for i in range(0, total_hotdogs, bundel):
        count = count + 1
    print(count)


# with_operators()
without_operators()
