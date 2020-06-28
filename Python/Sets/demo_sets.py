
def basic_of_sets():
    # Creating Sets
    s1 = set([1, 2, 3, 4, 5])
    print(s1)

    s1 = {1, 2, 3, 4, 5, 6}
    print(s1)

    # This creates an empty dict and not a set
    s1 = {}
    print(type(s1))

    # To create a empty set
    s1 = set()
    print(type(s1))

    # Removing the duplicate values
    s1 = {1, 2, 3, 4, 3, 2, 1, 1}
    print(s1)

    # Adding a single element to the set
    s1 = {1, 2}
    s1.add(4)
    print(s1)

    # Adding Multiple values to the Sets
    s1 = {1, 2, 3}
    s2 = {4, 5, 6}
    s1.update([99, 88], s2)
    print(s1)

    # Removing values from set
    s1 = {1, 2, 3, 4, 5}
    s1.remove(5)
    print(s1)

    # If the value we are trying to remove is not present in the list remove will give an error.
    # On the other hand discard will not give error

    # s1.remove(6)
    s1.discard(6)
    print(s1)


def useful_operations_with_sets():
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    s3 = {3, 4, 5}

    # Intersection will provide values which are there in both the sets
    s4 = s1.intersection(s2)
    s4 = s1.intersection(s2, s3)
    print(s4)

    # Difference will help to check if the values are present in 1 and not in other set.
    s4 = s1.difference(s2)
    s4 = s2.difference(s1)
    s4 = s2.difference(s1, s3)
    s4 = s1.difference(s2, s3)
    s4 = s3.difference(s1, s2)
    print(s4)

    # Symmetric difference will compare the sets and will give all diff values b/w the sets
    s4 = s1.symmetric_difference(s2)
    print(s4)


def practical_examples():
    # Removing Duplicates
    l1 = [1, 2, 3, 4, 2, 1, 0]
    l2 = list(set(l1))
    print(l2)

    employees = ['Corey', 'Jim', 'Steven',
                 'April', 'Judy', 'Jenn', 'John', 'Jane']
    gym_members = ['April', 'John', 'Corey']
    developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

    # Developers and have gym_membership
    results = set(developers).intersection(gym_members)
    print(results)

    # Neither Developers nor have a gym_membership
    results = set(employees).difference(developers, gym_members)
    print(results)

    # Sets have good performence in membership tests
    # O(n) for a list
    # O(1) for a set
    if 'Corey' in developers:
        print("FOUND!")

# basic_of_sets()
# useful_operations_with_sets()
# practical_examples()
