
def helper(data, low, high):
    pivot = data[low]
    i = low
    j = high
    while i < j:
        i += 1
        j -= 1
        while i < len(data):
            if data[i] > pivot:
                break
            i += 1
        while j >= 0:
            if data[j] <= pivot:
                break
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    if i >= j:
        data[low], data[j] = data[j], data[low]
    return j


def quicksort(data, low, high):
    if high > low:
        pi = helper(data, low, high)
        quicksort(data, low, pi)
        quicksort(data, pi+1, high)


mylist = [5, 7, 6, 9, 4, 8, 1, 2, 3]
quicksort(mylist, 0, len(mylist))
print(mylist)
