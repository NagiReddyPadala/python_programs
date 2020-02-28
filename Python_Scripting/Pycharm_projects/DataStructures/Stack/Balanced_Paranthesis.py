"""
Example: {[()]} - Balanced parenthis
          {]} - unbalanced parenthis
"""
from DataStructures.Stack.stack import Stack

def is_match(p1 , p2):
    if p1 == "{" and p2 == "}":
        return True
    elif p1 == "(" and p2 == ")":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in ['(', '[', '{']:
            s.push(paren)
        else:
            if not is_match(s.pop(), paren):
                is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        print("Given parenthesis '", paren_string, "' is balanced.")
    else:
        print("Given parenthesis '", paren_string, "' is not balanced.")


is_paren_balanced("({[]]})")
is_paren_balanced("({[]})")





