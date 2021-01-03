class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def delete(self, value):
        curr = self.head
        prev = self.head

        if self.head is not None:
            while curr:
                if curr.value == value and curr == self.head:
                    # Case if only 1 element is there and we need to delete it
                    if curr.next == self.head:
                        curr = None
                        self.head = None
                        return
                    # Case if more than  1 element is there and we need to delete head
                    else:
                        while curr.next != self.head:
                            curr = curr.next
                        curr.next = self.head.next
                        self.head = self.head.next
                        curr = None
                        return
                elif curr.value == value:
                    prev.next = curr.next
                    curr = None
                    return
                if curr.next == self.head:
                    print("Unable to find the value to delete")
                    return
                prev = curr
                curr = curr.next
        else:
            print("No element present in linked list to delete")

    def printall(self):
        tmp = self.head
        if self.head is not None:
            print("Printing Values in linked list")
            print("~~~~~~~~~~~~~~~")
            while True:
                print(tmp.value)
                tmp = tmp.next
                if tmp == self.head:
                    break
            print("~~~~~~~~~~~~~~~")
        else:
            print("No elements found in Linked List")

    def count(self):
        tmp = self.head
        count = 0
        if tmp is not None:
            while True:
                count += 1
                tmp = tmp.next
                if tmp == self.head:
                    break
        print("Total Values in Circular linked list is - {}".format(count))
        return count


if __name__ == '__main__':
    c1 = CircularLinkedList()
    c1.count()
    c1.push(1)
    c1.push(2)
    c1.push(3)
    c1.push(4)
    c1.printall()
    c1.delete(3)
    c1.printall()
