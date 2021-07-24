import gc


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

    def delete(self, value):
        tmp = self.head
        if self.head is None:
            print("Linked list is empty, nothing to delete")
            return
        else:
            while tmp is not None:
                # Case if this is a start of the node
                if tmp.value == value and self.head == tmp:
                    tmp.next.prev = tmp.prev
                    self.head = tmp.next
                    tmp = None
                    break
                # Case if this is a last node of the linked list
                elif tmp.value == value and tmp.next is None:
                    tmp.prev.next = tmp.next
                    tmp = None
                    break
                # Case if this is a node in the middle
                elif tmp.value == value:
                    tmp.prev.next = tmp.next
                    tmp.next.prev = tmp.prev
                    tmp = None
                    break
                tmp = tmp.next
            else:
                print("Unable to find the value to delete")
                return

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
    d1.append(1)
    d1.append(2)
    d1.append(3)
    d1.append(4)
    d1.append(5)
    d1.printall()
    d1.delete(9)
    d1.printall()
