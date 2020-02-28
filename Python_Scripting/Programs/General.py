def testgen(index):
    weekdays = ['sun','mon','tue','wed','thu','fri','sat']
    yield weekdays[index]
    yield weekdays[index+1]
day = testgen(0)
print (next(day), next(day))


weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)
print(type(listAsString))


weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
print(listAsTuple)
print(type(listAsTuple))


weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
listAsSet = set(weekdays)
print(listAsSet)
print(type(listAsSet))



weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays.count('mon'))


print([[x, weekdays.count(x)] for x in set(weekdays)])


import array
a = [1, 2, 3]
print (a[-3])


names = ['Chris', 'Jack', 'John', 'Daman']

print(names[-1][-1])


languages = ["python", "JS", "C", "C++"]
for i, lang in enumerate(languages):
    print(i, lang)


import random
list = [2, 18, 8, 4]
print ("Prior Shuffling - 0", list)

random.shuffle(list)
print ("After Shuffling - 1", list)

random.shuffle(list)
print ("After Shuffling - 2", list)

lst = []
lstLength = 10
for i in range(0, lstLength):
    lst.append(random.randrange(1,10))

print(lst)

test = "I am learning Python."
print (test.split(" "))

lst = "I am learning python".split()
print(lst)

print("***********************************")
item = [n*2 for n in range(10)]
print (item)


item = {n: n*2 for n in range(10)}
print (item)




class Test:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def __str__(self):
        return '{} holds ...'.format(self.name)
        
obj1 = Test('obj1')
print (obj1)
print(type(obj1))

obj2 = Test('obj2')
print (obj2)


def multiplexers ():
    res = [lambda n: index * n for index in range (4)]
    print(res)
    return res

print( [m (1) for m in multiplexers ()])


def fast (items= []):
    items.append (1)
    return items

print (fast ())
print (fast ())


wordList='1,3,2,4,5,3,2,1,4,3,2'.split(',')
print (wordList)

print([[x, wordList.count(x)] for x in set(wordList)])


def dic(wordList):
    wordlst = {}
    for degit in wordList:
        try:
            wordlst[degit] +=1
        except KeyError:
            wordlst[degit] =1
    return wordlst
        
 
wordList='1,3,2,4,5,3,2,1,4,3,2'.split(',')
print (wordList)

print (dic(wordList))


class Test(object):
    def __init__(self):
        self.x = 1
 
t = Test()
print (t.x)
print (t.x)
print (t.x)
print (t.x)
    
objects = {"python", "coding", "tips", "for", "beginners"}

# Print set.
print(objects)
print(len(objects))

# Use of "in" keyword.
if "tips" in objects:
    print("These are the best Python coding tips.")

# Use of "not in" keyword.
if "Java tips" not in objects:
    print("These are the best Python coding tips not Java tips.")


# *** Lets initialize an empty set
items = set()

# Add three strings.
items.add("Python")
items.add("coding")
items.add("tips") 

print(items)

# ** Output
{'Python', 'coding', 'tips'}


print('Python' + ' Interview' + ' Questions')


print (sum(range(1,101)))
print(random.randint(50,100))




globvar = 0
def set_globvar_to_one():
    global globvar # Needed to modify global copy of globvar
    globvar = 1
def print_globvar():
    print (globvar) # No need for global declaration to read value of globvar
set_globvar_to_one()
print_globvar() # Prints 1



names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print (sum)


list1 = [1, 3, 2]
print(list1*2)



#Can you write a program to find the average of numbers in a list in Python?
list1 = [1, 2, 3, 4,5]
sum = 0
for element in list1:
    sum += element
print(sum/len(list1))
    
"""
n=int(input("Enter number: "))
rev = 0
while (n>0):
    digit = n % 10
    rev = rev*10 + digit
    n = n//10
    
print("The reverse of the number:",rev)



n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


n = int(input("Please enter the number of the table: "))
for i in range(1, 11):
    print(n, " * ", i , " = ", n*i)

a=int(input("Enter number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k == 0):
    print("Number is prime")
else:
    print("Number isn't prime")



a=input("Enter number: ")
sum=0
for i in range(0, len(a)):
    sum += int(a[i])**3
if sum == int(a):
    print("armstrong")
else:
    print("not armstrong")
"""
"""
a=int(input("Enter number: "))
sum1 = 0
for i in range(1,a):
    if (a%i == 0):
        sum1 += i
if a == sum1:
    print("Perfect number")
else:
    print("Not perfect number")
"""

"""
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")
"""


a = [1, 2, 3, 4]
temp = a[0]
a[0] = a[len(a)-1]
a[len(a)-1] = temp

print(a)

str1 = "Nagi"
print(str1[::-1])


"""
sum1=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
while(i<=r):
    f=f*i
    i=i+1
    sum1=sum1+f
    num=num//10
if(sum1==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")

"""

class a:
    pass
obj=a()
obj.name="xyz"
print("Name = ",obj.name)


# Python program for implementation of Bubble Sort 

def bubbleSort(arr): 
	n = len(arr) 

	# Traverse through all array elements 
	for i in range(n): 

		# Last i elements are already in place 
		for j in range(0, n-i-1): 

			# traverse the array from 0 to n-i-1 
			# Swap if the element found is greater 
			# than the next element 
			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 

bubbleSort(arr) 

print ("Sorted array is:") 
for i in range(len(arr)): 
	print ("%d" %arr[i]), 


"""
# Enter number of terms needed                   #0,1,1,2,3,5....
a=int(input("Enter the terms: "))
f=0                                         #first element of series
s=1                                         #second element of series

if a<=0:
    print(f)
else:
    print(f, s, end = " ")
    for x in range(0, a):
        next = f+s
        print(next, end = " ")
        f = s
        s = next

"""

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    return a/b



res = div(2,4)
print(res)
