"""
Stack Data structure
Last in first out
"""

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

    def get_stack(self):
        return self.items

def reverse_string(stack, string):
    for char in string:
        stack.push(char)

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

s = Stack()
print(reverse_string(s, "Madhu"))

"""
s = Stack()
print("Before filling the stack: ", s.is_empty())
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
print(s.get_stack())
s.pop()
print(s.get_stack())
print("After filling the stack: ", s.is_empty())
print("Last element of the stack is: ", s.peek())"""
