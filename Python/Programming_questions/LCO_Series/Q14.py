"""
How many ways can four students "Ram", "Anuj", "Deepak" and "Ravi" line up in a line.
if the order matters?
Print all posible combinations.
"""


def via_predefined_functions():
    import itertools
    data = ['Ram', 'Anuj', 'Deepak', 'Ravi']
    results = itertools.permutations(data)
    for item in results:
        print(item)


# via_predefined_functions()


def creating_permutations_code(mylist):
    if len(mylist) == 0:
        return []

    if len(mylist) == 1:
        return [mylist]

    l = []
    for i in range(len(mylist)):
        m = mylist[i]
        remlst = mylist[:i] + mylist[i + 1:]
        for p in creating_permutations_code(remlst):
            l.append([m] + p)
    return l


data = ['Ram', 'Anuj', 'Deepak', 'Ravi']
for i in creating_permutations_code(data):
    print(i)
