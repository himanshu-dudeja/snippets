from queue import Queue

# Bad approach
def way1():
    mylist = []
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist)
    mylist.pop(0)
    print(mylist)
    mylist.pop(0)
    print(mylist)
    mylist.pop(0)
    print(mylist)
    mylist.pop(0)


def way2():
    from collections import deque
    mylist = deque()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist)
    mylist.popleft()
    print(mylist)
    mylist.popleft()
    print(mylist)
    mylist.popleft()
    print(mylist)
    mylist.popleft()


def way3():
    mylist = Queue()
    mylist.put(1)
    mylist.put(2)
    mylist.put(3)
    print(mylist.queue)
    mylist.get()
    print(mylist.queue)
    mylist.get()
    print(mylist.queue)
    mylist.get_nowait()
    print(mylist.queue)
    # mylist.get()  # This will create a block as it will be in a state to check if value is present
    mylist.get_nowait()


# way1()
# way2()
way3()

