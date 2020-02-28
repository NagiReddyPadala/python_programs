class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfterNode(self, prevNode, data):
        if not prevNode:
            print("Given node is not valid.")
            return

        new_node = Node(data)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def printllist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

llist = LinkedList()
print("After appending")
llist.append("A")
llist.append("B")
llist.printllist()
print("After prepending")
llist.prepend("C")
llist.printllist()
print("After Inserting")
llist.insertAfterNode(llist.head.next,"D")
llist.printllist()