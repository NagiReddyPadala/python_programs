class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        elif data > root.data:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)
        else:
            print("Value is already present in the tree")

    def find(self, data):
        if self.root:
            is_found = self._find(self.root, data)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, root, data):
        if root.data == data:
            return True
        if data < root.data and root.left:
            return self._find(root.left, data)
        elif data > root.data and root.right:
            return self._find(root.right, data)

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)
            if is_satisfied is None:
                return True
            return False
        return True

    def _is_bst_satisfied(self, root, data):
        if root.left:
            if data < root.left.data:
                return False
            return self._is_bst_satisfied(root.left, root.left.data)
        if root.right:
            if data > root.right.data:
                return False
            return self._is_bst_satisfied(root.right, root.right.data)



bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)
bst.insert(11)

tree = BinarySearchTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
# print(bst.find(4))
# print(bst.find(10))
# print(bst.find(11))

print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())