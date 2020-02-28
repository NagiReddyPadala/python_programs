str1 = "Nagireddy"

def remove_n_char(str1 ,n):
    str2 = ""
    for i in range(0, len(str1)):
        if not i+1 == n:
            str2 = str2 + str1[i]
    return str2

print(remove_n_char("Nagireddy", 2))


lst = [char for char in str1]
lst.pop(2-1)
print("".join(lst))

print(str1)
char = str1[1]

str2 = str1.replace(char,"",1)
print(str2)