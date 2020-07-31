
# Question -
# Find the best score using bubble sort for - [66, 57, 54, 53, 64, 52, 59]

def bubble_sort(mylist):
    print("Starting of List -> ", mylist)
    for i in range(1, len(mylist)):
        flag = 0
        for j in range(0, len(mylist) - i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
                flag = 1
                print("----->Internal-loop", mylist)
        print(mylist)
        if flag == 0:
            break
    print(mylist)


bubble_sort([66, 57, 54, 53, 64, 52, 59])
