"""
ABC
A BC
AB C
"""

string  = "ABC"

for i in range(len(string)):
    if i == 0:
        print(string)
    else:
        print(string[:i] + " " + string[i:])