import re

# initialising string
ini_string = "123()#$ABGFDabcjw"
ini_string2 = "abceddfgh"

print(ini_string)
print(ini_string2)

print("Extracting only chars:")

print("".join(re.findall("[a-zA-z]*", ini_string)))
print("".join(re.findall("[a-zA-z]*", ini_string2)))