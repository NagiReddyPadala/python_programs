test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

print("String 1: ", test_str1)
print("String 2: ", test_str2)

res = set(test_str1).symmetric_difference(test_str2)
print(res)

print("Uncommon chars are: ", str(res))
