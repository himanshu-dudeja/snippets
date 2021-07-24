def bubble(data: list):
    for i in range(len(data) - 1):
        print("Outer loop i = {}".format(i))
        for j in range(len(data) - (i+1)):
            print("inner loop j = {}".format(j))
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


print(bubble([40, 20, 50, 60, 30, 10]))
