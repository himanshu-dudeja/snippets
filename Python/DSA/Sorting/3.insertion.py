def insertion(data: list):
    for i in range(1, len(data)):
        temp = data[i]
        for j in range(i-1, -1, -1):
            if data[j] > temp:
                data[j+1] = data[j]
            else:
                data[j+1] = temp
                break
        else:
            data[0] = temp
    return data


print(insertion([9, 6, 7, 3, 2]))
