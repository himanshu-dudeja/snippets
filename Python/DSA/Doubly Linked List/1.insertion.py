class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, value):
        if prev_node is None:
            print("Prev Node is None can't proceed")
            return
        new_node = Node(value)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next = new_node
        if new_node.next is not None:
            tmp = new_node.next
            tmp.prev = new_node

    def append(self, value):
        last = self.head
        new_node = Node(value)
        if self.head is not None:
            while last.next is not None:
                last = last.next
            last.next = new_node
            new_node.prev = last
            return
        else:
            self.push(value)

    def printall(self):
        tmp = self.head
        if self.head is not None:
            print("Printing values in linked list")
            print("~~~~~~~~~~~~~~")
            while tmp is not None:
                print(tmp.value)
                tmp = tmp.next
            print("~~~~~~~~~~~~~~")
        else:
            print("Linked list is empty")


if __name__ == '__main__':
    d1 = DoublyLinkedList()
    d1.printall()
    d1.push(1)
    d1.push(2)
    d1.push(3)
    d1.push(4)
    d1.printall()
    d1.insert_after(d1.head, 55)
    d1.printall()
    d1.append(10)
    d1.printall()
