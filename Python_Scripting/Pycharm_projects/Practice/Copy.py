x = 10
y = x

print("x: ", x)
print("y: ", y)
print(id(x))
print(id(y))

x= 11

print("x: ", x)
print("y: ", y)
print(id(x))
print(id(y))

y = 12

print("x: ", x)
print("y: ", y)
print(id(x))
print(id(y))


lst1 = [1,2,3]
lst2 = lst1

print("lst1: ", lst1)
print("lst2: ", lst2)
print(id(lst1))
print(id(lst2))

lst2[2] = 4

print("lst1: ", lst1)
print("lst2: ", lst2)
print(id(lst1))
print(id(lst2))


print("====================================")
# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# using copy for shallow copy
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)

print("li1: ", li1)
print("li2: ", li2)
print("li3: ", li3)

print("li1: ", id(li1))
print("li2: ", id(li2))
print("li3: ", id(li3))

print("Changing shallow copy value")
li2[2][1] = 6

print("li1: ", li1)
print("li2: ", li2)
print("li3: ", li3)

print("li1: ", id(li1))
print("li2: ", id(li2))
print("li3: ", id(li3))

print("Changing deep copy value")
li3[2][1] = 7

print("li1: ", li1)
print("li2: ", li2)
print("li3: ", li3)

print("li1: ", id(li1))
print("li2: ", id(li2))
print("li3: ", id(li3))


print("**************************")

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy

print("xs: ", xs)
print("ys: ", ys)

print("id of xs: ", id(xs))
print("id of ys: ", id(ys))

xs.append(['new sublist'])

print("xs: ", xs)
print("ys: ", ys)

print("id of xs: ", id(xs[1]))
print("id of ys: ", id(ys[1]))

xs[1][0] = 'X'

print("xs: ", xs)
print("ys: ", ys)

print("id of xs: ", id(xs[1]))
print("id of ys: ", id(ys[1]))


xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = copy.deepcopy(xs)  # Make a shallow copy

print("xs: ", xs)
print("ys: ", ys)

print("id of xs: ", id(xs[1]))
print("id of ys: ", id(ys[1]))

ys[1][0] = 'X'

print("xs: ", xs)
print("ys: ", ys)

print("id of xs: ", id(xs[1]))
print("id of ys: ", id(ys[1]))


xs = [1,2,3,4]
ys = copy.copy(xs)

print("xs: ", xs)
print("ys: ", ys)
print("id of xs: ", id(xs))
print("id of ys: ", id(ys))

ys[1] = 'X'

print("xs: ", xs)
print("ys: ", ys)

print("id of xs: ", id(xs))
print("id of ys: ", id(ys))
