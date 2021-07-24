class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, this_node, data):
        if this_node.data > data:
            if this_node.left is None:
                this_node.left = Node(data)
            else:
                self.insert_helper(this_node.left, data)
        else:
            if this_node.right is None:
                this_node.right = Node(data)
            else:
                self.insert_helper(this_node.right, data)

    def get_inorder_successor(self, this_node):
        # inorder successor will calculate the smallest from the right
        # Assuming that "this_node" provided will be the right node
        myval = this_node
        while myval.left is not None:
            myval = myval.left
        return myval

    def get_inorder_predesessor(self, this_node):
        # inorder predessor will calculate the largest from the left
        # Assuming that "this_node" provided will be the left node
        myval = this_node
        while myval.right is not None:
            myval = myval.right
        return myval

    def delete(self, this_node, data):
        if this_node is None:
            return this_node
        if data < this_node.data:
            this_node.left = self.delete(this_node.left, data)
        elif data > this_node.data:
            this_node.right = self.delete(this_node.right, data)
        else:
            # Case for either 1 or 0 child
            if this_node.left is None:
                temp = this_node.right
                this_node = None
                return temp
            elif this_node.right is None:
                temp = this_node.left
                this_node = None
                return temp
            # Case for 2 child
            temp = self.get_inorder_successor(this_node.right)
            this_node.data = temp.data
            this_node.right = self.delete(this_node.right, temp.data)
        return this_node

    def search(self, this_node, data):
        if this_node is None:
            print("data not found")
            return False
        elif this_node.data == data:
            print("data - {} found".format(data))
            return True
        elif data < this_node.data:
            self.search(this_node.left, data)
        elif data > this_node.data:
            self.search(this_node.right, data)

    def inorder(self, this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.data, end=" ")
            self.inorder(this_node.right)

    def preorder(self, this_node):
        if this_node:
            print(this_node.data, end=" ")
            self.preorder(this_node.right)
            self.preorder(this_node.left)

    def postorder(self, this_node):
        if this_node:
            self.postorder(this_node.right)
            self.postorder(this_node.left)
            print(this_node.data, end=" ")


if __name__ == '__main__':
    b1 = BinarySearchTree()
    b1.insert(11)
    b1.insert(12)
    b1.insert(13)
    b1.insert(10)
    b1.insert(10.3)
    b1.insert(1)
    b1.insert(3)
    b1.inorder(b1.get_root())
    print("\n")
    b1.delete(b1.get_root(), 12)
    b1.inorder(b1.get_root())
    print("\n")
    b1.delete(b1.get_root(), 11)
    b1.inorder(b1.get_root())
