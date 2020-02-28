# Examples of Arithmetic Operator 
a = 9
b = 4

# Addition of numbers 
add = a + b 
# Subtraction of numbers 
sub = a - b 
# Multiplication of number 
mul = a * b 
# Division(float) of number 
div1 = a / b 
# Division(floor) of number 
div2 = a // b 
# Modulo of both number 
mod = a % b 

# print results 
print(add) 
print(sub) 
print(mul) 
print(div1) 
print(div2) 
print(mod) 



# Examples of Relational Operators 
a = 13
b = 33

# a > b is False 
print(a > b) 

# a < b is True 
print(a < b) 

# a == b is False 
print(a == b) 

# a != b is True 
print(a != b)


# a >= b is False 
print(a >= b) 

# a <= b is True 
print(a <= b) 



# Examples of Logical Operator 
a = True
b = False

# Print a and b is False 
print(a and b) 

# Print a or b is True 
print(a or b) 

# Print not a is False 
print(not a) 


# Examples of Bitwise operators 
a = 10
b = 4

# Print bitwise AND operation 
print(a & b) 

# Print bitwise OR operation 
print(a | b) 

# Print bitwise NOT operation 
print(~a) 

# print bitwise XOR operation 
print(a ^ b) 

# print bitwise right shift operation 
print(a >> 2) 

# print bitwise left shift operation 
print(a << 2) 



print("*******************************************************")
# Examples of Bitwise operators 
a = 10
b = 4

# Print bitwise AND operation 
print(a & b) 

# Print bitwise OR operation 
print(a | b) 

# Print bitwise NOT operation 
print(~a) 

# print bitwise XOR operation 
print(a ^ b) 

# print bitwise right shift operation 
print(a >> 2) 

# print bitwise left shift operation 
print(a << 2) 


a=15
print(a)
print(a>>2)
print(a<<2)


# Examples of Identity operators 
a1 = 3
b1 = 3
a2 = 'GeeksforGeeks'
b2 = 'GeeksforGeeks'
a3 = [1,2,3] 
b3 = [1,2,3] 


print(a1 is not b1) 


print(a2 is b2) 

# Output is False, since lists are mutable. 
print(a3 is b3) 



# A Python program that uses Bitwise Not or ~ on boolean 
a = True
b = False
print (~a) 
print (~b)



# Python program to demonstrate ternary operator 
a, b = 10, 20

# Use tuple for selecting an item 
print((b, a) [a < b]) 

# Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 

# lamda is more efficient than above two methods 
# because in lambda we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]())


print (5/2)
print (-5/2)
print (5.0/2)
print (-5.0/2)


print (5//2)
print (-5//2)
print (5.0//2)
print (-5.0//2)


class A:
    def __init__(self, a):
        self.a = a
        print(self.a)
    def __add__(self, o):
        return self.a + o.a

ob1 = A(1)
ob2 = A(2)

ob3 = A("Hello")
ob4 = A("Hi")

print(ob1 + ob2)
print(ob3 + ob4)


# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading. 

class complex: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	# adding two objects 
	def __add__(self, other): 
		return self.a + other.a + 1, self.b + other.b + 1 

	 

Ob1 = complex(1, 2) 
Ob2 = complex(2, 3) 
Ob3 = Ob1 + Ob2 
print(Ob3) 

# Since all are false, false is returned 
print (any([False, False, False, False])) 

# Here the method will short-circuit at the 
# second item (True) and will return True. 
print (any([False, True, False, False])) 

# Here the method will short-circuit at the 
# first (True) and will return True. 
print (any([True, False, False, False]))


# Python code to demonstrate difference between 
# Inplace and Normal operators in Immutable Targets 

# importing operator to handle operator operations 
import operator 

# Initializing values 
x = 5
y = 6
a = 5
b = 6

# using add() to add the arguments passed 
z = operator.add(a,b) 

# using iadd() to add the arguments passed 
p = operator.iadd(x,y) 

# printing the modified value 
print ("Value after adding using normal operator : ",end="") 
print (z) 

# printing the modified value 
print ("Value after adding using Inplace operator : ",end="") 
print (p) 

# printing value of first argument 
# value is unchanged 
print ("Value of first argument using normal operator : ",end="") 
print (a) 

# printing value of first argument 
# value is unchanged 
print ("Value of first argument using Inplace operator : ",end="") 
print (x) 



# Python code to demonstrate difference between 
# Inplace and Normal operators in mutable Targets 

# importing operator to handle operator operations 
import operator 

# Initializing list 
a = [1, 2, 4, 5] 

# using add() to add the arguments passed 
z = operator.add(a,[1, 2, 3]) 

# printing the modified value 
print ("Value after adding using normal operator : ",end="") 
print (z) 

# printing value of first argument 
# value is unchanged 
print ("Value of first argument using normal operator : ",end="") 
print (a) 

# using iadd() to add the arguments passed 
# performs a+=[1, 2, 3] 
p = operator.iadd(a,[1, 2, 3]) 

# printing the modified value 
print ("Value after adding using Inplace operator : ",end="") 
print (p) 

# printing value of first argument 
# value is changed 
print ("Value of first argument using Inplace operator : ",end="") 
print (a) 



list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 += [1, 2, 3, 4] 

print(list1) 
print(list2) 


list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 = list1 + [1, 2, 3, 4] 

# Contents of list1 are same as above 
# program, but contents of list2 are 
# different. 
print(list1) 
print(list2) 



# python3 code to 
# illustrate the 
# difference between 
# == and is operator 
# [] is an empty list 
list1 = [] 
list2 = [] 
list3=list1
print("List1 id: ", id(list1))
print("List2 id: ", id(list2))
print("List3 id: ", id(list2))


if (list1 == list2): 
	print("True") 
else: 
	print("False") 

if (list1 is list2): 
	print("True") 
else: 
	print("False") 

if (list1 is list3): 
	print("True") 
else:	 
	print("False") 
