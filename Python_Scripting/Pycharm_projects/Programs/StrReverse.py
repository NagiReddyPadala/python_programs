str = "Nagireddy"

#print(str[::-1])

for i in range(len(str), 0 , -1):
    print(str[i-1], end="")

print()

def rev_string(s):
    rev_str = ""
    for char in s:
        rev_str =  char + rev_str
    return rev_str

print(rev_string("Madhu"))




# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string

print(reverse("Hello"))

