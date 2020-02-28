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
        new_node = Node(data)
        new_node.next = prevNode.next
        prevNode.next = new_node

    def delete_node(self, data):
        cur_node = self.head

        if cur_node and cur_node.data == data:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None

        while cur_node and cur_node.data != data:
            prev_node = cur_node
            cur_node = cur_node.next

        if prev_node:
            prev_node.next = cur_node.next
            cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 1

        while cur_node and count <= pos:
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1

        if prev_node:
            prev_node.next = cur_node.next
            cur_node = None

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node:
            cur_node = cur_node.next
            count += 1

        print("Length of the linked list is: ", count)
        return count

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next

        if not cur1 or not cur2:
            return

        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        cur1.next, cur2.next = cur2.next, cur1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev


    def recursive_reverse(self):
        def _recursive_reverse(curr, prev):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            return  _recursive_reverse(curr, prev)

        self.head = _recursive_reverse(curr = self.head, prev = None)


    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p


    def remove_duplicates(self):
        cur_node = self.head
        prev_node = None

        dup_values = dict()

        while cur_node:
            if cur_node.data in dup_values:
                prev_node.next = cur_node.next
                cur_node = None
            else:
                dup_values[cur_node.data] = 1
                prev_node = cur_node
            cur_node = prev_node.next

    def print_nth_from_last(self, n):
        total_len = self.length()

        cur_node = self.head
        while cur_node:
            if total_len == n:
                print(cur_node.data)
                return
            total_len -= 1
            cur_node = cur_node.next

        if cur_node is None:
            return

    def count_occurances_iterative(self, val):
        cur_node = self.head
        count = 0
        while cur_node:
            if cur_node.data == val:
                count += 1
            cur_node = cur_node.next
        return count

    def count_occurances_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurances_recursive(node.next, data)
        else:
            return  self.count_occurances_recursive(node.next, data)

    def rotate(self, k):
        p = self.head
        q = self.head

        prev = None
        count = 0
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1

        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def move_tail_to_head(self):
        last = self.head
        second_to_last = None

        while last.next:
            second_to_last = last
            last = last.next

        last.next = self.head
        second_to_last.next = None
        self.head = last


    def printllist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# llist = LinkedList()
# print("Head is: ", llist.head)
# llist.append("A")
# print("Head is: ", llist.head)
# llist.append("B")
# llist.append("C")
# llist.append("D")
"""
print("Head is: ", llist.head)
llist.printllist()
print("Head is: ", llist.head)
llist.prepend("C")
llist.printllist()
llist.insertAfterNode(llist.head.next,"D")
print("**********")
llist.printllist()
print("*************")
#llist.delete_node("D")
#llist.delete_node_at_pos(1)
llist.printllist()
llist.length()
print("After swappig")
llist.swap_nodes("C", "B")
llist.printllist()
"""
#llist.reverse_iterative()
#llist.printllist()
#
# print("After recursive reverse")
# llist.recursive_reverse()
# llist.printllist()

# llist1 = LinkedList()
#
# llist1.append(1)
# llist1.append(3)
# llist1.append(5)
# llist1.append(7)
#
# llist2 = LinkedList()
# llist2.append(2)
# llist2.append(4)
# llist2.append(6)
# llist2.append(8)
#
# print(llist1.printllist())
# print(llist2.printllist())
#
# llist1.merge_sorted(llist2)
#
# print(llist1.printllist())


#
# llist1 = LinkedList()
#
# llist1.append(1)
# llist1.append(2)
# llist1.append(1)
# llist1.append(2)
# llist1.append(3)
# llist1.printllist()
# llist1.remove_duplicates()
# print("***********")
# llist1.printllist()




# llist1 = LinkedList()
#
# llist1.append(1)
# llist1.append(2)
# llist1.append(3)
# llist1.append(4)
# llist1.append(5)
# llist1.printllist()
# print("***********")
# llist1.print_nth_from_last(2)


# llist1 = LinkedList()
#
# llist1.append(1)
# llist1.append(2)
# llist1.append(1)
# llist1.append(2)
# llist1.append(3)
#
# print(llist1.count_occurances_iterative(1))
# print(llist1.count_occurances_iterative(2))
# print(llist1.count_occurances_iterative(3))
# print("***********")
#
# print(llist1.count_occurances_recursive(llist1.head, 1))
# print(llist1.count_occurances_recursive(llist1.head, 2))
# print(llist1.count_occurances_recursive(llist1.head, 3))

#
# llist1 = LinkedList()
#
# llist1.append(1)
# llist1.append(2)
# llist1.append(3)
# llist1.append(4)
# llist1.append(5)
# llist1.append(6)
#
# llist1.rotate(4)
# llist1.printllist()


llist1 = LinkedList()

llist1.append(1)
llist1.append(2)
llist1.append(3)
llist1.append(4)

llist1.move_tail_to_head()
llist1.printllist()
