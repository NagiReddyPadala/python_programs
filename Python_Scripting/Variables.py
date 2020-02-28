# A Python program to demonstrate that we can store 
# large numbers in Python 

x = 10000000000000000000000000000000000000000000; 
x = x + 1
print (x, type(x))


# This function uses global variable s 
def f(): 
	print (s) 

# Global scope 
s = "I love Geeksforgeeks"
f()


# This function has a variable with 
# name same as s. 
def f(): 
	s = "Me too."
	print (s) 

# Global scope 
s = "I love Geeksforgeeks"
f() 
print (s)


print("*************************************************")

def f():
    global s
    print (s)
    # This program will NOT show error
    # if we comment below line.
    s = "Me too."
    print (s)

# Global scope 
s = "I love Geeksforgeeks"
f() 
print (s) 


# A Python program to demonstrate need 
# of packing and unpacking 

# A sample function that takes 4 arguments 
# and prints them. 
def fun(a, b, c, d): 
	print(a, b, c, d) 

# Driver Code 
my_list = [1, 2, 3, 4] 

# This doesn't work 
fun(*my_list)


# A Python program to demonstrate both packing and 
# unpacking. 

# A sample python function that takes three arguments 
# and prints them 
def fun1(a, b, c): 
	print(a, b, c) 

# Another sample function. 
# This is an example of PACKING. All arguments passed 
# to fun2 are packed into tuple *args. 
def fun2(*args):
    # Convert args tuple to a list so we can modify it
    print(type(args))
    args = list(args) 
    print(type(args))
    # Modifying args 
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'

    # UNPACKING args and calling fun1() 
    fun1(*args) 

# Driver code 
fun2('Hello', 'beautiful', 'world!')



# A sample program to demonstrate unpacking of 
# dictionary items using ** 
def fun(a, b, c): 
	print(a, b, c) 

# A call with unpacking of dictionary 
d = {'a':2, 'b':4, 'c':10} 
fun(**d) 


# A Python program to demonstrate packing of 
# dictionary items using ** 
def fun(**kwargs): 

	# kwargs is a dict 
	print(type(kwargs)) 

	# Printing dictionary items 
	for key in kwargs: 
		print("%s = %s" % (key, kwargs[key])) 

# Driver code 
fun(name="geeks", ID="101", language="Python") 


# Python code to demonstrate Type conversion 
# using int(), float() 

# initializing string 
s = "10010"

# printing string converting to int base 2 
c = int(s,2) 
print ("After converting to integer base 2 : ", end="") 
print (c) 

# printing string converting to float 
e = float(s) 
print ("After converting to float : ", end="") 
print (e)


# Python code to demonstrate Type conversion 
# using ord(), hex(), oct() 

# initializing integer 
s = '4'

# printing character converting to integer 
c = ord(s) 
print ("After converting character to integer : ",end="") 
print (c) 

# printing integer converting to hexadecimal string 
c = hex(56) 
print ("After converting 56 to hexadecimal string : ",end="") 
print (c) 

# printing integer converting to octal string 
c = oct(56) 
print ("After converting 56 to octal string : ",end="") 
print (c) 


# Python code to demonstrate Type conversion 
# using tuple(), set(), list() 

# initializing string 
s = 'geeks'

# printing string converting to tuple 
c = tuple(s) 
print ("After converting string to tuple : ",end="") 
print (c) 

# printing string converting to set 
c = set(s) 
print ("After converting string to set : ",end="") 
print (c) 

# printing string converting to list 
c = list(s) 
print ("After converting string to list : ",end="") 
print (c) 


# Python code to demonstrate Type conversion 
# using dict(), complex(), str() 

# initializing integers 
a = 1
b = 2

# initializing tuple 
tup = (('a', 1) ,('f', 2), ('g', 3)) 

# printing integer converting to complex number 
c = complex(1,2) 
print ("After converting integer to complex number : ",end="") 
print (c) 

# printing integer converting to string 
c = str(a) 
print ("After converting integer to string : ",end="") 
print (c) 

# printing tuple converting to expression dictionary 
c = dict(tup) 
print ("After converting tuple to dictionary : ",end="") 
print (c) 



# Python code to demonstate String encoding 

# initialising a String 
a = 'GeeksforGeeks'
print(a)

# initialising a byte object 
c = b'GeeksforGeeks'
print(c)

# using encode() to encode the String 
# encoded version of a is stored in d 
# using ASCII mapping 
d = a.encode('ASCII')
print(d)

# checking if a is converted to bytes or not 
if (d==c): 
	print ("Encoding successful") 
else : print ("Encoding Unsuccessful")


# Python code to demonstate Byte Decoding 

# initialising a String 
a = 'GeeksforGeeks'

# initialising a byte object 
c = b'GeeksforGeeks'

# using decode() to decode the Byte object 
# decoded version of c is stored in d 
# using ASCII mapping 
d = c.decode('ASCII') 

# checking if c is converted to String or not 
if (d==a): 
	print ("Decoding successful") 
else : print ("Decoding Unsuccessful") 


x = 5
y = 10
x,y = y,x
print(x,y)



# File1.py
import Data_Types

print ("File1 __name__ = %s" %__name__)

if __name__ == "__main__": 
	print ("File1 is being run directly")
else: 
	print ("File1 is being imported")







