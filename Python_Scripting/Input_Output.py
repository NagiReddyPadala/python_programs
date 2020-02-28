"""
# Python program showing  
# a use of input() 
  
val = input("Enter your value: ") 
print(val)
print(type(val))



# Python program showing how to 
# multiple input using split 
  
# taking two inputs at a time 
x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 


# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split() 
print("Total number of students: ", x) 
print("Number of boys is : ", y) 
print("Number of girls is : ", z) 
print() 
  
# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print()


x = list(map(float, input("Enter values: ").split()))
print(x)
for val in x:
    print(type(val))



x, y = [int(x) for x in input("Enter two numbers: ").split()]
print (x)
print (y)
print("First number is {}, second number is {}".format(x,y))


n = input("Enter the no.of numberas: ")
lNum = [int(x) for x in input("Enter the numbers: ").split()]

Sum = 0

for num in lNum:
    Sum +=num

print("Sum is: ", Sum)

from sys import stdin, stdout
n = stdin.readline()
lNum = [int(x) for x in stdin.readline().split()]

Sum = 0

for num in lNum:
    Sum +=num
print("Sum is: ", Sum)


# 3 inputs using input() function, 
# after which data type of the value 
# entered is displayed 
s4 = input("Enter input to test input() function: ") 
print (type(s4)) 

s5 = input("Enter input to test input() function: ") 
print (type(s5)) 

s6 = input("Enter input to test input() function: ") 
print (type(s6))


import random 
secret_number = random.randint(1,500) 
print ("Pick a number between 1 to 500")
while True: 
    res = input("Guess the number: ") 
    if res==secret_number: 
        print ("You win")
        break
    else: 
        print ("You lose")
        continue


# Python 2.x program showing 
# how to print data on 
# a screen 

# One object is passed 
print ("GeeksForGeeks")

# Four objects are passed 
print ("Geeks", "For", "Geeks", "Portal")

l = [1, 2, 3, 4, 5] 
# printing a list 
print (l)



# Python 3.x program showing 
# how to print data on 
# a screen 

# One object is passed 
print("GeeksForGeeks") 

x = 5
# Two objects are passed 
print("x =", x) 

# code for disabling the softspace feature 
print('G', 'F', 'G', sep ='  ') 

# using end argument 
print("Python", end = '@') 
print("GeeksforGeeks")



# This Python program must be run with 
# Python 3 as it won't work with 2.7. 

# ends the output with a <space> 
print("Welcome to" , end = ' ') 
print("GeeksforGeeks")




#code for disabling the softspace feature 
print('G','F','G', sep='') 
  
#for formatting a date 
print('09','12','2016', sep='-') 
  
#another example 
print('pratik','geeksforgeeks', sep='@') 

"""

# Python program showing how to use 
# string modulo operator(%) to print 
# fancier output 

# print integer and float value 
print("Geeks : % 2d, Portal : % 0.2f" %(1000, 05.333)) 

# print integer value 
print("Total students : % 3d, Boys : % 2d" %(240, 120)) 

# print octal value 
print("% 7.3o"% (25)) 

# print exponential value 
print("% 10.3E"% (356.08977))


# Python program showing 
# use of format() method 

# using format() method 
print('I love {} for "{}!"'.format('Geeks', 'Geeks')) 

# using format() method and refering 
# a position of the object 
print('{0} and {1}'.format('Geeks', 'Portal')) 

print('{1} and {0}'.format('Geeks', 'Portal'))



# Python program showing 
# a use of format() method 

# combining positional and keyword arguments 
print('Number one portal is {0}, {1}, and {other}.'
	.format('Geeks', 'For', other ='Geeks')) 

# using format() method with number 
print("Geeks :{0:2d}, Portal :{1:0.1f}". 
	format(121212, 88.546)) 

# Changing positional argument 
print("Second argument: {1:3d}, first one: {0:7.1f}". 
	format(47.42, 11)) 

print("Geeks: {a:5d}, Portal: {p:8.2f}". 
	format(a = 453, p = 59.058))


# Python program to 
# format a output using 
# string() method 

cstr = "I love geeksforgeeks"
	
# Printing the center aligned 
# string with fillchr 
print ("Center aligned string with fillchr: ") 
print (cstr.center(40, '#')) 

# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ") 
print (cstr.ljust(40, '-')) 

# Printing the right aligned string 
# with "-" padding 
print ("The right aligned string is : ") 
print (cstr.rjust(40, '-')) 






