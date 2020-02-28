class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.items = []

    def enque(self, item):
        self.items.insert(0, item)

    def deque(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def get_stack(self):
        return self.items



class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_print(self, start, traversal):
        """Root-> Left -> Right"""
        if start:
            traversal += str(start.value) + " -> "
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + " -> "
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + " -> "
        return traversal

    def levelorder_print(self, start):
        "Print level wise"
        if start is None:
            return

        queue = Queue()
        queue.enque(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + " -> "
            node = queue.deque()

            if node.left:
                queue.enque(node.left)
            if node.right:
                queue.enque(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        "Print level wise"
        if start is None:
            return

        queue = Queue()
        queue.enque(start)
        stack = Stack()
        traversal = ""
        while len(queue) > 0:
            #traversal += str(queue.peek()) + " -> "
            node = queue.deque()
            stack.push(node)

            if node.right:
                queue.enque(node.right)
            if node.left:
                queue.enque(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + " -> "

        return traversal

        return traversal

    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self):
        if tree.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        count = 1

        while stack:
            node = stack.pop()
            if node.left:
                count +=1
                stack.push(node.left)
            if node.right:
                count += 1
                stack.push(node.right)
        return count

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)



    def print_tree(self, travesal_type):
        if travesal_type == "preorder":
            return  self.preorder_print(tree.root, "")
        elif travesal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif travesal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif travesal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif travesal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)

        else:
            return "Traversal type " + str(travesal_type) + " is not supported"






tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))
print()
print(tree.print_tree("inorder"))
print()
print(tree.print_tree("postorder"))
print()
print(tree.print_tree("levelorder"))
print()
print(tree.print_tree("reverse_levelorder"))
print()
print("Height of 1: " + str(tree.height(tree.root)))
print("Height of 2: " + str(tree.height(tree.root.left)))
print("Height of 4: " + str(tree.height(tree.root.left.left)))

print("Size of tree is: " + str(tree.size()))
print("Size of tree is: " + str(tree.size_recursive(tree.root)))