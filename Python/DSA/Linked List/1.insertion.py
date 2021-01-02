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

    def printall(self):
        tmp = self.head
        while tmp:
            print(tmp.value)
            tmp = tmp.next


if __name__ == '__main__':
    l1 = LinkedList()
    l1.push(5)
    l1.append(7)
    l1.push(6)
    l1.insertat(l1.head, 8)
    l1.insert_at_position(3, 77)
    l1.printall()
