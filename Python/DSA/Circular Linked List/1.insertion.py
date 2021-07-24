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


if __name__ == '__main__':
    c1 = CircularLinkedList()
    c1.push(1)
    c1.push(2)
    c1.push(3)
    c1.printall()
