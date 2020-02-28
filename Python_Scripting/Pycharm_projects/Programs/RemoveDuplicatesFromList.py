lst1 = [1,1, 2, 3, 2, 4, 3 ]

lst2 = []

for val in lst1:
    if val not in lst2:
        lst2.append(val)

print(lst2)

lst3 = []
[lst3.append(val) for val in lst1 if val not in lst3]
print(lst3)


lst4 = []
lst1 = [1,1, 2, 3, 2, 4, 3 ]
for val in lst1:
    if val in lst4:
        print("Duplicates exists")
        break
    else:
        lst4.append(val)

