
def selection_my_way(my_list):
    print("Starting List -> ", my_list)
    for i in range(0, len(my_list)):
        # Find min val
        min_val = min(my_list[i:])
        index = my_list.index(min_val, i)
        # Swap min val with the start of unsorted list
        my_list[i], my_list[index] = my_list[index], my_list[i]
        print(my_list)


def selection(my_list):
    print("Starting List ->", my_list)
    for i in range(0, len(my_list)):
        min_val = my_list[i]
        for j in range(i + 1, len(my_list)):
            if min_val > my_list[j]:
                min_val = my_list[j]
                index = j
        if min_val != my_list[i]:
            my_list[index], my_list[i] = my_list[i], my_list[index]
        print(my_list)


def selection_my_way_desc(my_list):
    print("Starting List -> ", my_list)
    for i in range(0, len(my_list)):
        # Find min val
        min_val = max(my_list[i:])
        index = my_list.index(min_val, i)
        # Swap min val with the start of unsorted list
        my_list[i], my_list[index] = my_list[index], my_list[i]
        print(my_list)


selection_my_way([56, 4, 24, 16, 5, 45])
selection([1, 56, 4, 24, 16, 5, 45, 1, 1])
selection_my_way_desc([1, 56, 4, 24, 16, 5, 45, 1, 1])
