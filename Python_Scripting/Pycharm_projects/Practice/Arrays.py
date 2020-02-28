import array as arr

vals = arr.array('i', [1,2,8,4])
#new_Arr = vals
new_Arr = arr.array(vals.typecode, (a*a for a in vals))

print(vals.buffer_info())
print(vals.typecode)
#vals.reverse()
print(vals)
print(vals[0])

for i in range(4):
    print(vals[i])

for i in range(len(vals)):
    print(vals[i])

for val in vals:
    print(val)

print(sorted(vals))

print(new_Arr)


ar = arr.array('i', [])
len = int(input("Please enter the length of array: "))
for i in range(len):
    val = int(input("Please enter the value: "))
    ar.append(val)

#index = int(input("Please enter the index to delete: "))
#del ar[index]
print(ar[::-1])

for i in range(len):
    print(ar[len-i-1])