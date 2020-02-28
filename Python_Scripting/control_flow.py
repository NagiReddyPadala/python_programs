#Python program to illustrate 
# combining else with while 
count = 0
while (count < 3):	 
	count = count + 1
	print("Hello Geek") 
else: 
	print("In Else Block") 


#How to print a list in reverse order (from last to first item) using while and for in loops.

l1 = [1,2,3,4,5,6,7,8,9]
lLen = len(l1)
length = 1
while length <= lLen:
    print(l1[-length])
    length +=1


# python code to demonstrate working of enumerate() 

for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']): 
	print(key, value) 
# python code to demonstrate working of zip() 

# initializing list 
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle'] 


print(zip(questions, answers))
# using zip() to combine two containers 
# and print values 
for question, answer in zip(questions, answers): 
	print('What is your {0}? I am {1}.'.format(question, answer)) 



# python code to demonstrate working of iteritems(),items() 

d = { "geeks" : "for", "only" : "geeks" } 

# using iteritems to print the dictionary key-value pair 
print ("The key value pair using iteritems is : ") 
#for i,j in d.iteritems(): 
#	print (i,j) 
	
# using items to print the dictionary key-value pair 
print ("The key value pair using items is : ") 
for i,j in d.items(): 
	print (i,j) 


# python code to demonstrate working of sorted() 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 

# using sorted() to print the list in sorted order 
print ("The list in sorted order is : ") 
for i in sorted(lis) : 
	print (i,end=" ") 
	
print ("\r") 
	
# using sorted() and set() to print the list in sorted order 
# use of set() removes duplicates. 
print ("The list in sorted order (without duplicates) is : ") 
for i in sorted(set(lis)) : 
	print (i,end=" ")


# python code to demonstrate working of sorted() 

# initializing list 
basket = ['guave', 'orange', 'apple', 'pear', 
		'guava', 'banana', 'grape'] 

# using sorted() and set() to print the list 
# in sorted order 
for fruit in sorted(set(basket)): 
	print(fruit)



# python code to demonstrate working of reversed() 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, 1, 3 ] 


# using revered() to print the list in reversed order 
print ("The list in reversed order is : ") 
for i in reversed(lis) : 
	print (i,end=" ")

print("\n")


for i in range(1,6):
    print ('* '*i)

print("\n")
print("\n")


def printStar(rows):
    for i in range(1,rows+1):
        for j in range(0,i):
            print("*", end=" ")
        print("\n")
printStar(5)

print("**************************************************************************")

def printStarReverse(rows):
    space = 2*rows-2
    for i in range(0,rows):
        for j in range(0,space):
            print(end=" ")
        for j in range(0,i+1):
            print("* ", end="")
        print("\r")
        space-=2
x = range(0,1)
print(x)
printStarReverse(5)



# Python 3.x code to demonstrate star pattern 

# Function to demonstrate printing pattern triangle 
def triangle(n): 
	
	# number of spaces 
	k = 2*n - 2

	# outer loop to handle number of rows 
	for i in range(0, n): 
	
		# inner loop to handle number spaces 
		# values changing acc. to requirement 
		for j in range(0, k): 
			print(end=" ") 
	
		# decrementing k after each loop 
		k = k - 1
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ", end="") 
	
		# ending line after each row 
		print("\r") 

# Driver Code 
n = 5
triangle(n) 



# Function to convert number into string 
# Switcher is dictionary data type here 
def numbers_to_strings(argument): 
	switcher = { 
		0: "zero", 
		1: "one", 
		2: "two", 
	} 

	# get() method of dictionary data type returns 
	# value of passed argument if it is present 
	# in dictionary otherwise second argument will 
	# be assigned as default value of passed argument 
	return switcher.get(argument, "nothing") 

# Driver program 
if __name__ == "__main__": 
	argument=0
	print (numbers_to_strings(argument))

            



# A simple Python program to demonstrate 
# working of iterators using an example type 
# that iterates from 10 to given value 

class Test:
    def __init__(self, limit):
        self.limit = limit
        

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x+1
        return x
        

# Prints numbers from 10 to 15 
for i in Test(15): 
    print(i) 
  
# Prints nothing 
for i in Test(5): 
    print(i)


# Python code demonstrating 
# basic use of iter() 
listA = ['a','e','i','o','u'] 

iter_listA = listA.__iter__() 

try: 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) 
	print( next(iter_listA)) #StopIteration error 
except: 
	pass


def feb(num):
    a,b = 0,1

    while a < num:
        yield a
        a,b = b, a+b

for i in feb(5):
    print (i, end = " ")



# Python code to illustrate generator, yield() and next(). 
def generator(): 
	t = 1
	print ('First result is ',t )
	yield t 

	t += 1
	print ('Second result is ',t )
	yield t 

	t += 1
	print ('Third result is ',t )
	yield t 

call = generator() 
next(call) 
next(call) 
next(call)

call1 = generator() 
next(call1) 
next(call1) 
next(call1)


mygenerator = (x*x for x in range(3))
print(mygenerator)
for i in mygenerator:
    print(i)

print(mygenerator)
for i in mygenerator:
    print(i)
print("**************************************")
def ownGen():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygen = ownGen()
for i in mygen:
    print(i)

for i in mygen:
    print(i)


