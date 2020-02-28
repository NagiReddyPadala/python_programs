"""
Use a stack data structure to convert integer values to binary
242 / 2 = 121 -> 0
121 / 2 = 60  -> 1
60 / 2 = 30   -> 0
30 / 2 = 15   -> 0
15/ 2 = 7     -> 1
7 / 2 = 3     -> 1
3 / 2 = 1     -> 1
1 / 2 = 0     -> 1
"""


from DataStructures.Stack.stack import Stack

def get_binary(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)

        dec_num = dec_num // 2

    binary_num = ""

    while not s.is_empty():
        binary_num += str(s.pop())

    print("Binary number is: ", binary_num)

get_binary(242)

