a = [1, 2, 3]

try:
    print("Second element is: ", a[1])
    print("Fourth element is: ", a[3])


except IOError:
    print("IO Error")

except IndexError:
    print("Index error")

except:
    print("General Error")
else:
    print("No error")


# Program to depict Raising Exception 

try:
    raise NameError("Hi there") # Raise Error 
except NameError as error:
    print (error)
    #raise # To determine whether the exception was raised or not


class MyError(Exception):
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return(self.val)

try:
    raise(MyError(3*2))
except MyError as error:
    print("My own error val: ", error.val)


#help(Exception)

#assert True, 'The assertion failed'


class Attributes(object): 
	pass

object = Attributes() 
#print (object.val)

#while True:
#    data = input('Enter name : ')
#    print ('Hello ', data)

import math 

print (math.exp(2)) 


# Python code to illustrate 
# clean up actions 
def divide(x, y): 
	try: 
		# Floor Division : Gives only Fractional Part as Answer 
		result = x // y 
	except ZeroDivisionError: 
		print("Sorry ! You are dividing by zero ") 
	else: 
		print("Yeah ! Your answer is :", result) 
	finally: 
		print("I'm finally clause, always raised !! ") 

# Look at parameters and note the working of Program 
#divide(3, "3") 

n = int(input()) 
k = int(input()) 
print (n," ",k)



