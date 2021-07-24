def counting(data: list):
        max_val = max(data)
        temp_list = [None for _ in range(max_val+1)]

        for ele in data:
            if temp_list[ele] is None:
                temp_list[ele] = 1
            else:
                temp_list[ele] = temp_list[ele] + 1
        print(temp_list)

        counter = 0
        for index in range(len(temp_list)):
            if temp_list[index] is not None:
                while temp_list[index] != 0:
                    temp_list[index] -= 1
                    data[counter] = index
                    counter += 1


mylist = [5, 3, 2, 3, 6, 1]
counting(mylist)
print(mylist)
