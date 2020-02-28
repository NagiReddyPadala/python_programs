str1 = "Nagireddy"
n = 4

def remove_n_chars(str1, n):
    str2 = ""
    for i in range(0, len(str1)):
        if i >= n:
            str2 =  str2 + str1[i]
    return str2

print(remove_n_chars(str1, 4))

print(str1[4:])

print(str1[2::2])