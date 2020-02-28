str = "asdhsaddffdnsadsaasdshdkAAA"
dict = {}
for char in str:
    #char = char.lower()
    dict[char] = dict.get(char, 0) + 1

print(dict['a'])
print(dict['A'])


str1 = "abccba"
str2 = str1[0:len(str1)//2]
str3 = str1[len(str1)//2:]

print(str1)
print(str2)
print(str3)

for char in str2:
    if char not in str3:
        print("Same chars not present in both string")

input = "ABCDEFG"
length = len(input)

# Break input string in two parts
if (length % 2 != 0):
    first = input[0:length // 2]
    second = input[(length // 2) + 1:]
else:
    first = input[0:length // 2]
    second = input[length // 2:]

print(first)
print(second)
