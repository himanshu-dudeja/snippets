def selection(data: list):
    for i in range(len(data)):
        min_index = i
        for _i in range(i+1, len(data)):
            if data[min_index] > data[_i]:
                min_index = _i
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
    return data


print(selection([1, 34, 2, 5, 77, 3]))
