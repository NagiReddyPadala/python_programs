for x in range(1, 5): 
    print(x), 


y = 3
z = 10

print(100 or 20 or 30 or 10 or 70)
print(0 or 0 or 3 or 10 or 0)

print (None == 0)


x = None
y = None
print (x == y)



# Python code to demonstrate  
# del and assert 
  
# initialising list  
a = [1, 2, 3] 
  
# printing list before deleting any value 
print ("The list before deleting any value") 
print (a)

# using del to delete 2nd element of list 
del a[1] 
  
# printing list after deleting 2nd element 
print ("The list after deleting 2nd element") 
print (a) 

del a
#print(a) #NameError: name 'a' is not defined, since we deleted a


# demonstrating use of assert 
# prints AssertionError 
#assert 5<3, "5 is not smaller than 3."


# Python code to demonstrate working of 
# in and is 
  
# using "in" to check  
if 's' in 'geeksforgeeks':
    print ("s is part of geeksforgeeks") 
else:
    print ("s is not part of geeksforgeeks")


# using "in" to loop through 
for i in 'geeksforgeeks': 
    print (i,end=",") 
  
print ("\r")


# using is to check object identity 
# string is immutable( cannot be changed once alloted) 
# hence occupy same memory location 
print (' ' is ' ')


# using is to check object identity 
# dictionary is mutable( can be changed once alloted) 
# hence occupy different memory location 
print ({} is {})


#initializing variable globally 
a = 10
  
# used to read the variable 
def read():
    print (a)

# changing the value of globally defined variable 
def mod1(): 
    global a  
    a = 5
    
# changing value of only local variable 
def mod2():
    #global a
    a = 15

# reading initial value of a 
# prints 10 
read() 
  
# calling mod 1 function to modify value 
# modifies value of global a to 5 
mod1() 
  
# reading modified value 
# prints 5 
read() 
  
# calling mod 2 function to modify value 
# modifies value of local a to 15, doesn't effect global value 
mod2() 
  
# reading modified value 
# again prints 5 
read()


# demonstrating non local  
# inner loop changing the value of outer a 
# prints 10 
print ("Value of a using nonlocal is : ",end="") 
def outer(): 
    a = 5
    def inner(): 
        nonlocal a  
        a = 10
    inner() 
    print (a) 
  
outer()


# demonstrating without non local  
# inner loop not changing the value of outer a 
# prints 5 
print ("Value of a without using nonlocal is : ",end="") 
def outer(): 
    a = 5
    def inner(): 
        a = 10
    inner() 
    print (a) 
  
outer()


# var1 is in the global namespace  
var1 = 5
def some_func(): 
  
    # var2 is in the local namespace  
    var2 = 6
    def some_inner_func(): 
  
        # var3 is in the nested local  
        # namespace 
        var3 = 7


# Python program processing 
# global variable 
  
count = 5
def some_method(): 
    global count 
    count = count + 1
    print(count) 
some_method()


# Python program showing 
# a scope of object 
  
def some_func(): 
    print("You are welcome to some_func") 
    #print(var) 
some_func()

# Python program showing 
# a scope of object 
  
def some_func(): 
    print("Inside some_func") 
    def some_inner_func(): 
        var = 10
        print("Inside inner function, value of var:",var) 
    some_inner_func() 
    print("Try printing var from outer function: ") 
some_func()



#Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print ("Sum (S) is: ",format(s))
print(type(s))

#Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 8 + 9)
print(n)
print(type(n))

#Declared using square brackets [] :
footballer = ['MESSI',
          'NEYMAR',
          'SUAREZ']
print(footballer)
print(type(footballer))

#Declared using braces {} :
x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}
print(x)
print(type(x))

#Declared using semicolons(;) :
flag = 2; ropes = 3; pole = 4

  
# Python program showing 
# indentation 
  
site = 'gfg'
  
if site == 'gfg': 
    print('Logging on to geeksforgeeks...') 
else: 
    print('retype the URL.') 
print('All set !')



j = 1
while(j<= 5): 
	print(j) 
	j = j + 1

# This is a comment 
# Print “GeeksforGeeks !” to console 
print("GeeksforGeeks")





a, b = 1, 3 # Declaring two integers 
sum = a + b # adding two integers 
print(sum) # displaying the output 


""" 
This would be a multiline comment in Python that 
spans several lines and describes geeksforgeeks. 
A Computer Science portal for geeks. It contains 
well written, well thought 
and well-explained computer science 
and programming articles, 
quizzes and more.  
"""
print("GeeksForGeeks") 



'''This article on geeksforgeeks gives you a 
perfect example of 
multi-line comments'''

print("GeeksForGeeks") 



# Example 1 
  
print('Welcome to Geeks for Geeks')


# Example 2 

x = [1, 2, 3, 4] 

# x[1:3] means that start from the index 
# 1 and go upto the index 2 
print(x[1:3]) 

""" In the above mentioned format, the first 
index is included, but the last index is not 
included."""


# Example 

a = 10; b = 20; c = b + a 

print(a); print(b); print(c)



# Bad Practice as width of this code is
# too much.

#code
x = 10
y = 20
z = 30
no_of_teachers = x
no_of_male_students = y
no_of_female_students = z

if (no_of_teachers == 10 and no_of_female_students == 30 and no_of_male_students == 20
    and (x + y) == 30):
        print('The course is valid')



# Example 1 

# The following code is valid 
a = [ 
	[1, 2, 3], 
	[3, 4, 5], 
	[5, 6, 7] 
	] 

print(a)



# Example 2 
# The following code is also valid 

person_1 = 18
person_2 = 20
person_3 = 12

if ( 
person_1 >= 18 and
person_2 >= 18 and
person_3 < 18
): 
	print('2 Persons should have ID Cards') 




#Python code to demonstrate working of iskeyword() 

# importing "keyword" for keyword operations 
import keyword 

# initializing strings for testing 
s = "for"
s1 = "geeksforgeeks"
s2 = "elif"
s3 = "elseif"
s4 = "nikhil"
s5 = "assert"
s6 = "shambhavi"
s7 = "True"
s8 = "False"
s9 = "akshat"
s10 = "akash"
s11 = "break"
s12 = "ashty"
s13 = "lambda"
s14 = "suman"
s15 = "try"
s16 = "vaishnavi"

# checking which are keywords 
if keyword.iskeyword(s): 
		print ( s + " is a python keyword") 
else : print ( s + " is not a python keyword") 

if keyword.iskeyword(s1): 
		print ( s1 + " is a python keyword") 
else : print ( s1 + " is not a python keyword") 

if keyword.iskeyword(s2): 
		print ( s2 + " is a python keyword") 
else : print ( s2 + " is not a python keyword") 

if keyword.iskeyword(s3): 
		print ( s3 + " is a python keyword") 
else : print ( s3 + " is not a python keyword") 

if keyword.iskeyword(s4): 
		print ( s4 + " is a python keyword") 
else : print ( s4 + " is not a python keyword") 

if keyword.iskeyword(s5): 
		print ( s5 + " is a python keyword") 
else : print ( s5 + " is not a python keyword") 

if keyword.iskeyword(s6): 
		print ( s6 + " is a python keyword") 
else : print ( s6 + " is not a python keyword") 

if keyword.iskeyword(s7): 
		print ( s7 + " is a python keyword") 
else : print ( s7 + " is not a python keyword") 

if keyword.iskeyword(s8): 
		print ( s8 + " is a python keyword") 
else : print ( s8 + " is not a python keyword") 

if keyword.iskeyword(s9): 
		print ( s9 + " is a python keyword") 
else : print ( s9 + " is not a python keyword") 

if keyword.iskeyword(s10): 
		print ( s10 + " is a python keyword") 
else : print ( s10 + " is not a python keyword") 

if keyword.iskeyword(s11): 
		print ( s11 + " is a python keyword") 
else : print ( s11 + " is not a python keyword") 

if keyword.iskeyword(s12): 
		print ( s12 + " is a python keyword") 
else : print ( s12 + " is not a python keyword") 

if keyword.iskeyword(s13): 
		print ( s13 + " is a python keyword") 
else : print ( s13 + " is not a python keyword") 

if keyword.iskeyword(s14): 
		print ( s14 + " is a python keyword") 
else : print ( s14 + " is not a python keyword") 

if keyword.iskeyword(s15): 
		print ( s15 + " is a python keyword") 
else : print ( s15 + " is not a python keyword") 

if keyword.iskeyword(s16): 
		print ( s16 + " is a python keyword") 
else : print ( s16 + " is not a python keyword")


import keyword as kw
name = "nagi"
if kw.iskeyword(name):
    print("Nagi is a keyword")
else:
    print("Nagi is not a keyword")

print(kw.kwlist)



# Python 3 code to demonstrate variable assignment 
# upon condition using One liner if-else 

# initialising variable using Conditional Operator 
# a = 20 > 10 ? 1 : 0 is not possible in Python 
# Instead there is one liner if-else 
a = 1 if 5 < 20 else 2

# printing value of a 
print ("The value of a is: " + str(a))


# Python 3 code for printing 
# on the same line printing 
# geeks and geeksforgeeks 
# in the same line 

print("geeks", end =" ") 
print("geeksforgeeks") 

# array 
a = [1, 2, 3, 4] 

# printing a element in same 
# line 
for i in range(4): 
	print(a[i], end=",")


# python program to illustrate If statement 

i = 10
if (i > 15): 
    print ("10 is less than 15") 
print ("I am Not in if")



# python program to illustrate If else statement 
#!/usr/bin/python 

i = 20; 
if (i < 15): 
	print ("i is smaller than 15") 
	print ("i'm in if Block") 
else: 
	print ("i is greater than 15") 
	print ("i'm in else Block") 
print ("i'm not in if and not in else Block")




# python program to illustrate nested If statement 
#!/usr/bin/python 
i = 10
if (i == 10): 
	# First if statement 
	if (i < 15): 
		print ("i is smaller than 15") 
	# Nested - if statement 
	# Will only be executed if statement above 
	# it is true 
	if (i < 12): 
		print ("i is smaller than 12 too") 
	else: 
		print ("i is greater than 15")


# Python program to illustrate if-elif-else ladder 
#!/usr/bin/python 

i = 20
if (i == 10): 
	print ("i is 10") 
elif (i == 15): 
	print ("i is 15") 
elif (i == 20): 
	print ("i is 20") 
else: 
	print ("i is not present")


def Add(num1, num2):
    return num1+num2

def Subtract(num1, num2):
    return num1-num2

def Mutiply(num1, num2):
    return num1-num2

def Devide(num1, num2):
    return num1-num2

print("Please select operation - \n" \
        "1. Add \n" \
        "2. Subtract \n" \
        "3. Multiply \n" \
        "4. Devide \n")

selectedOperation = input("Selecte operations from 1, 2, 3, 4 : " )
num1 = int(input("Enter first number: " ))
num2 = int(input("Enter second number: " ))

if  selectedOperation == "1":
    print(num1, "+", num2, "=",
          Add(num1, num2))
elif selectedOperation == "2":
    print(Subtract(num1, num2))
elif selectedOperation == "3":
    print(Mutiply(num1, num2))
elif selectedOperation == "4":
    print(Devide(num1, num2))
else:
    print("Selected operation is invalid")


x = 12
y = 13
print(x, "+", y, "=", (x+y))












