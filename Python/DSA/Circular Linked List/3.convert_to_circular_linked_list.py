class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insertat(self, prev_node, value):
        if prev_node is None:
            print("Previous value is empty")

        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_at_position(self, position, value):
        if self.head is None:
            print("Linked list is empty, inserting this value as the first node")
            self.push(value)
            return

        tmp = self.head
        index = 1
        while tmp:
            if index == int(position) - 1:
                new_node = Node(value)
                new_node.next = tmp.next
                tmp.next = new_node
                print("Added value {} to position {}".format(value, position))
                break
            index += 1
            tmp = tmp.next
        else:
            print("Unable to find position {} in the LinkedList, inserting at end".format(position))
            self.append(value)

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deletenode(self, value):
        tmp = self.head

        # Case if the Linked List is empty
        if tmp is None:
            print("LinkedList is empty, no value is present to delete")
            return

        # Case if we need to delete the first node of linked list
        if self.head is not None and tmp.value == value:
            self.head = tmp.next
            tmp = None
            return

        # Case if we need to delete node from any mid/end place
        while tmp:
            if tmp.value == value:
                break
            prev = tmp
            tmp = tmp.next
        else:
            print("Value {} not found in the linked list".format(value))
            return
        prev.next = tmp.next
        tmp = None

    def delete_entire_linkedlist(self):
        cur = self.head
        while cur:
            new = cur.next
            del cur
            self.head = new
            cur = new

    def printall(self):
        tmp = self.head

        print("Printing all values")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        while tmp:
            print(tmp.value)
            tmp = tmp.next
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

    def countall(self):
        tmp = self.head

        index = 0
        while tmp:
            index += 1
            tmp = tmp.next
        print("Total nodes in linked list are - {}".format(index))

    def count_with_recursion(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.count_with_recursion(node.next)

    def countall2(self):
        print("Total nodes in linked list counted via recursion is - {}".format(self.count_with_recursion(self.head)))

    def convert_to_circular(self, start):
        head = start
        if start:
            while start.next is not None:
                start = start.next
            start.next = head
        else:
            print("Linked list is empty")


if __name__ == '__main__':
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(5)
    l1.printall()
    l1.convert_to_circular(l1.head)
    # l1.printall() # This will be infinite to prove that its now a circular linked list.

