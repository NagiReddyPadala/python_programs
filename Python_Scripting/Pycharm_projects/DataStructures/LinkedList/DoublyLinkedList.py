class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.next = None
            new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_after(self, key, data):
        new_node = Node(data)
        cur = self.head
        if cur.data == key and not cur.next:
            self.append(data)
            # self.head.next = new_node
            # new_node.prev = self.head
        else:
            while cur.next:
                if cur.data == key:
                    break
                cur = cur.next

            new_node.prev = cur
            new_node.next = cur.next
            cur.next = new_node

    def add_before(self, key, data):
        new_node = Node(data)
        cur = self.head
        prev = Node
        if cur.data == key and not cur.prev:
            self.prepend(data)
            # self.head.next = new_node
            # new_node.prev = self.head
        else:
            while cur.next:
                if cur.data == key:
                    break
                prev = cur
                cur = cur.next

            prev.next = new_node
            new_node.prev = prev
            new_node.next = cur
            cur.prev = new_node

    def delete(self, key):
        cur = self.head
        prev = None

        if cur.data == key and not cur.prev:
            cur.next.prev = None
            self.head = cur.next
            return

        while cur:
            if cur.data == key:
                break
            prev = cur
            cur = cur.next
        if not cur.next:
            prev.next = None
        else:
            prev.next = cur.next
            cur.next.prev = prev

    def reverse(self):
        temp = None
        cur = self.head

        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        if temp:
            self.head = temp.prev

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next

dlist = DoublyLinkedList()
dlist.append("A")
dlist.append("B")
dlist.append("C")
dlist.append("D")

#dlist.prepend("E")
#dlist.add_after("D", "E")
#dlist.add_before("D", "E")

#dlist.delete("D")
dlist.reverse()
dlist.print_list()
