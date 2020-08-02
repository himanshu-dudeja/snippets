"""
There are 10 students in a class and some names of students are same.
Find the names of students which occur more than once.
All names should be in single string.

Eg str = 'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar'
"""


def find_same_names(mystr):
    mylist = mystr.split()
    ans_list = []
    for ele in mylist:
        if mylist.count(ele) > 1:
            ans_list.append(ele)
    print(" ".join(set(ans_list)))


find_same_names(
    'Aman Ankit Deepak Arjun Nakul Amit Priyanshu Vansh Rajat Sagar')


def second_way(mystr):
    from collections import Counter
    output = Counter(mystr.split())
    ans_list = list()
    for i, j in output.items():
        if j > 1:
            ans_list.append(i)
    print(" ".join(ans_list))


second_way('Aman Aman Deepak Arjun Nakul Deepak Priyanshu Nakul Rajat Sagar')


def another_way(mystr):
    mylist = mystr.split()
    l = list()
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i] == mylist[j] and mylist[i] not in l:
                l.append(mylist[i])
    print(l)


another_way('Aman Aman Deepak')
