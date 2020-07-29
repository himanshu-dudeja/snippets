
def insertion(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (j >= 0 and my_list[j] > temp):
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = temp
        print(my_list)

    print("END->", my_list)


# insertion([2, 45, 6, 34])

def insertion_my_way(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        del(my_list[i])
        for j in range(i - 1, -1, -1):
            if my_list[j] > temp and j == 0:
                my_list.insert(j, temp)
                break
            elif my_list[j] > temp:
                continue
            else:
                my_list.insert(j + 1, temp)
                break
        print(my_list)
    print("END->", my_list)


# insertion_my_way([2, 45, 6, 34])
# insertion_my_way([2, 1, 6, 34, 4, 3])


def insertion_desc_order(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (j >= 0 and my_list[j] < temp):
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = temp
        print(my_list)

    print("END->", my_list)


insertion_desc_order([2, 45, 6, 34, 110])
