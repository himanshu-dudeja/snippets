
def asec_order_bubble(my_list):
    n = len(my_list)
    for i in range(1, n):
        for index in range(0, n - i):
            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index +
                                        1] = my_list[index + 1], my_list[index]
    print(my_list)


# asec_order_bubble([34, 333, 555, 444, 5, 77, 33, 24, 78])

def desc_order_bubble(my_list):
    n = len(my_list)
    for i in range(1, n):
        for j in range(0, n - i):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(my_list)


# desc_order_bubble([1, 34, 333, 555, 444, 5, 77, 33, 24, 78])

def desc_order_bubble_only_using_greater_than_operator(my_list):
    n = len(my_list)
    for i in range(1, n):
        for index in range(0, n - i):
            if my_list[index] > my_list[index + 1]:
                pass
            else:
                my_list[index], my_list[index +
                                        1] = my_list[index + 1], my_list[index]
    print(my_list)


# desc_order_bubble_only_using_greater_than_operator(
#     [2, 3, 1, 34, 333, 555, 444, 5, 77, 33, 24, 78])


# What if the iter is done in first few loops only instead of all the iterations
def asec_order_bubble_with_flag(my_list):
    n = len(my_list)
    for i in range(1, n):
        flag = 0
        for index in range(0, n - i):
            if my_list[index] > my_list[index + 1]:
                my_list[index], my_list[index +
                                        1] = my_list[index + 1], my_list[index]
                flag = 1
        if flag == 0:
            print("Iteration completed before itself -> all passes not req.")
            break
    print(my_list)


# asec_order_bubble_with_flag([2, 3, 1, 34, 333, 555, 444, 5, 77, 33, 24, 78])
asec_order_bubble_with_flag([121, 33, 32, 27, 30, 23, 4, 3, 1])
