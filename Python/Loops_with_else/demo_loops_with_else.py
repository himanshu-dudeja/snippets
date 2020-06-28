
# Else statement in loops are triggered when the loop terminates without triggering break statement
# (Else statement naming to nobreak)

def basic_example1():
    my_list = [1, 2, 3, 4]
    for i in my_list:
        print(i)
        # if i == 3:
        #     break
    else:
        print("Hit the For/Else statement")


def basic_example2():
    i = 1
    while i <= 5:
        print(i)
        i += 1
        # if i == 3:
        #     break
    else:
        print("Hit the For/Else statement")


def real_world_example():
    def find_index(to_search, target):
        for i, value in enumerate(to_search):
            if value == target:
                break
        else:
            return -1
        return i

    my_list = ["AA", "BB", "CC"]
    index_location = find_index(my_list, "BB")

    print(index_location)


# basic_example1()
# basic_example2()
real_world_example()
