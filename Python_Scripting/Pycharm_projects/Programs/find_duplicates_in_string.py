def print_duplicates(string):
    count = 0
    res_dict = {}
    for char in string:
        res_dict[char] = res_dict.get(char, 0) + 1

    for key, val in res_dict.items():
        if val > 1:
            print(key, end=" ")
    print()

def print_duplicates1(string):
    lst  = []
    for char in string:
        if char not in lst and string.count(char) > 1:
            lst.append(char)
            print(char, end=" ")
    print()


from collections import Counter
def find_dup_char(input):
    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)

    for key, val in WC.items():
        if val > 1:
            print(key, end=" ")




print_duplicates1("hello")
print_duplicates1("geeksforgeeeks")
print_duplicates1("Nagireddy")
find_dup_char("geeksforgeeeks")
