"""
a = "This is a string"
print (a)
a = "Hello"
print (a)


l = [1, "a", "string", 1+2]
print (l)
l.append(6)
print (l)
l.pop()
print (l)
print (l[1])
l[1] = 2
print (l[1])


t =(1, "a", "string", 1+2)
print (t)
print (t[1])
print (t)


i = 1
while (i < 10): 
	i += 1
	print (i, end=" ")
print ("\n")


s = "Hello world"
for ch in s:
    print (ch)


L = [1, 4, 5, 7, 8, 9] 
for i in L: 
	print (i)

x = range(0,5)
print (type(x))
for i in range(0, 10): 
	print (i) 




# Python Program for 
# Creation of String 

# Creating a String 
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 

# Creating a String 
# with double Quotes 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 

# Creating a String 
# with triple Quotes 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 

# Creating String with triple 
# Quotes allows multiple lines 
String1 = '''Geeks 
	     For 
	     Life'''
print("\nCreating a multiline String: ") 
print(String1)


# Python Program to Access 
# characters of String 

String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 

# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 

# Printing Last character 
print("\nLast character of String is: ") 
print(String1[-13])


# Python Program to 
# demonstrate String slicing 

# Creating a String 
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 

# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 

# Printing characters between 
# 3rd and 2nd last character 
print("\nSlicing characters between " +
	"3rd and 2nd last character: ") 
print(String1[3:-2])


# Python Program to Update 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a character 
# of the String 
# String1[2] = 'p'
print("\nUpdating character at 2nd Index: ") 
print(String1)


# Python Program to Update 
# entire String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a String 
String1 = "Welcome to the Geek World"
print("\nUpdated String: ") 
print(String1) 


# Python Program to Delete 
# characters from a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Deleting a character 
# of the String 
# del String1
print("\nDeleting character at 2nd Index: ") 
print(String1) 

# Python Program for 
# Escape Sequencing 
# of String 

# Initial String 
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 

# Escaping Single Quote 
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ") 
print(String1) 

# Escaping Doule Quotes 
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ") 
print(String1) 

# Printing Paths with the 
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1) 


# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1)



# Python Program for 
# Formatting of Strings 

# Default order 
String1 = "{},{},{}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g = 'Geeks', f = 'For', l = 'Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 

# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1)


# String alignment 
String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks','for','Geeks') 
print("\nLeft, center and right alignment with Formatting: ") 
print(String1) 

# To demonstrate aligning of spaces 
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009) 
print(String1)

newStr = "Hello,Hi,How,are,you"
print(newStr.split(","))


lst = []
print(lst)


lst = ['Hello']
print(lst)


lst = ['hello', 'hi', 'how']
print(lst)
print(lst[0])
print(lst[2])


lst = [['hello','hi'], ['Nagi', 'Madhu']]
print(lst[0])
print(lst[0][1])
print(lst[1][1])



# Python program to demonstrate 
# Addition of elements in a List 

# Creating a List 
List = [] 
print("Initial blank List: ") 
print(List) 

# Addition of Elements 
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 

# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
	List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 

# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 

# Addition of List to a List 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 


# Python program to demonstrate 
# Addition of elements in a List 

# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# Addition of Element at 
# specific Position 
# (using Insert Method) 
List.insert(3, 12) 
List.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List)


# Python program to demonstrate 
# Addition of elements in a List 
	
# Creating a List 
List = [1,2,3,4] 
print("Initial List: ") 
print(List) 

# Addition of multiple elements 
# to the List at the end 
# (using Extend Method) 
List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List)



# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = [1, 2, 3, 4, 5, 5, 6, 
		7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 

# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 

# Removing elements from List 
# using iterator method 
for i in range(1, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 



List = [1,2,3,4,5] 

# Removing element from the 
# Set using the pop() method 
print("popped element", List.pop()) 
print("\nList after popping an element: ") 
print(List) 

# Removing element at a 
# specific location from the 
# Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List)



# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Intial List: ") 
print(List) 

# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) #K','S','F', 'O','R',

# Print elements from a 
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
	"element till the end: ") 
print(Sliced_List) #'F', 'O','R','G','E','E','K','S'

# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) #full


# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Initial List: ") 
print(List) 

# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) #'G','E','E','K','S','F', 'O'

# Print elements of a range 
# using negative index List slicing 
Sliced_List = List[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(Sliced_List)  #'R','G','E','E','K'

# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) #Reverse

List = [1, 1, 2, 3, 4]
print(List.count(1))
print(type(1))
print(type("String"))
#print(List.min())
#print(List.max())

#Creation of Python tuple without the use of parentheses is known as Tuple Packin

# Python program to demonstrate 
# Addition of elements in a Set 

# Creating an empty tuple 
Tuple1 = () 
print("Initial empty Tuple: ") 
print (Tuple1) 

# Creating a Tuple with 
# the use of Strings 
Tuple1 = ('Geeks', 'For') 
print("\nTuple with the use of String: ") 
print(Tuple1) 

# Creating a Tuple with 
# the use of list 
list1 = [1, 2, 4, 5, 6] 
print("\nTuple using List: ") 
print(tuple(list1)) 

# Creating a Tuple 
# with the use of loop 
Tuple1 = ('Geeks') 
n = 5
print("\nTuple with a loop") 
for i in range(int(n)): 
	Tuple1 = (Tuple1,1) 
	print(Tuple1) 

# Creating a Tuple with the 
# use of built-in function 
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1) 

# Creating a Tuple with 
# Mixed Datatypes 
Tuple1 = (5, 'Welcome', 7, 'Geeks') 
print("\nTuple with Mixed Datatypes: ") 
print(Tuple1) 

# Creating a Tuple 
# with nested tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('python', 'geek') 
Tuple3 = (Tuple1, Tuple2) 
print("\nTuple with nested tuples: ") 
print(Tuple3) 

# Creating a Tuple 
# with repetition 
Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ") 
print(Tuple1)



# Concatenaton of tuples 
Tuple1 = (0, 1, 2, 3) 
Tuple2 = ('Geeks', 'For', 'Geeks') 

Tuple3 = Tuple1 + Tuple2 

# Printing first Tuple 
print("Tuple 1: ") 
print(Tuple1) 

# Printing Second Tuple 
print("\nTuple2: ") 
print(Tuple2) 

# Printing Final Tuple 
print("\nTuples after Concatenaton: ") 
print(Tuple3) 


t1 = 1, 2, 3, "Four"
print(t1)
print(t1[0])



# Python program to demonstrate 
# Creation of Set in Python 

# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 

# Creating a Set with 
# the use of a String 
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 

# Creating a Set with 
# the use of Constructor 
# (Using object to Store String) 
String = 'GeeksForGeeks'
set1 = set(String) 
print("\nSet with the use of an Object: " ) 
print(set1) 

# Creating a Set with 
# the use of a List 
set1 = set(["Geeks", "For", "Geeks"]) 
print("\nSet with the use of List: ") 
print(set1) 

print(type(t1))



# Creating a Set with 
# a List of Numbers 
# (Having duplicate values) 
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
print("\nSet with the use of Numbers: ") 
print(set1) 

# Creating a Set with 
# a mixed type of values 
# (Having numbers and strings) 
set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("\nSet with the use of Mixed Values") 
print(set1) 


# Python program to demonstrate 
# Addition of elements in a Set 

# Creating a Set 
set1 = set() 
print("Intial blank Set: ") 
print(set1) 

# Adding element and tuple to the Set 
set1.add(8) 
set1.add(9) 
set1.add((6,7)) 
print("\nSet after Addition of Three elements: ") 
print(set1) 

# Adding elements to the Set 
# using Iterator 
for i in range(1, 6): 
	set1.add(i) 
print("\nSet after Addition of elements from 1-5: ") 
print(set1)


# Python program to demonstrate 
# Addition of elements in a Set 

# Addition of elements to the Set 
# using Update function 
set1 = set([ 4, 5, (6, 7)]) 
set1.update([10, 11]) 
print("\nSet after Addition of elements using Update: ") 
print(set1) 


# Python program to demonstrate 
# Accessing of elements in a set 

# Creating a set 
set1 = set(["Geeks", "For", "Geeks"]) 
print("\nInitial set") 
print(set1) 

# Accessing element using 
# for loop 
print("\nElements of set: ") 
for i in set1: 
	print(i, end=" ") 

# Checking the element 
# using in keyword 
print("Geeks" in set1) 


# Python program to demonstrate 
# Deletion of elements in a Set 

# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6, 
			7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 

# Removing elements from Set 
# using Remove() method 
set1.remove(5) 
set1.remove(6) 
print("\nSet after Removal of two elements: ") 
print(set1) 

# Removing elements from Set 
# using Discard() method 
set1.discard(8) 
set1.discard(9) 
print("\nSet after Discarding two elements: ") 
print(set1) 

# Removing elements from Set 
# using iterator method 
for i in range(1, 5): 
	set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1) 


set1 = {1, 2, 3}
print(set1)
#print(set1[0])
print(type(set1))


# Python program to demonstrate 
# Deletion of elements in a Set 

# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6, 
			7, 8, 9, 10, 11, 12]) 
print("Intial Set: ") 
print(set1) 

# Removing element from the 
# Set using the pop() method 
set1.pop() 
print("\nSet after popping an element: ") 
print(set1) 


#Creating a set 
set1 = set([1,2,3,4,5]) 
print("\n Initial set: ") 
print(set1) 


# Removing all the elements from 
# Set using clear() method 
set1.clear() 
print("\nSet after clearing all the elements: ") 
print(set1) 


# Python program to demonstrate 
# working of a FrozenSet 

# Creating a Set 
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 

Fset1 = frozenset(String) 
print("The FrozenSet is: ") 
print(Fset1) 

# To print Empty Frozen Set 
# No parameter is passed 
print("\nEmpty FrozenSet: ") 
print(frozenset()) 

l1 = ["Hello"]
print(l1)
"""

# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Creating a Dictionary 
# with Integer Keys 
Dict = {1: 'Geeks',
        2: 'For',
        3: 'Geeks'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with Mixed keys 
Dict = {'Name': 'Geeks',
        1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict) 

# Creating a Dictionary 
# with dict() method 
Dict = dict({1: 'Geeks',
             2: 'For',
             3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 

# Creating a Dictionary 
# with each item as a Pair 
Dict = dict([(1, 'Geeks'), (2, 'For'), ('key', 'value')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


Dict = {1: "one",
        2: "two",
        3: "three",
        'Alphabates': {'a': "apple",
                     'b': "ball",
                     'c': "cat"}}
print(Dict)


# Creating an empty Dictionary 
Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 

# Adding elements one at a time 
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Adding set of values 
# to a single Key 
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ") 
print(Dict) 

# Updating existing Key's Value 
Dict[2] = 'Welcome'
print("\nUpdated key value: ") 
print(Dict) 

# Adding Nested Key value to Dictionary 
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}} 
print("\nAdding a Nested Key: ") 
print(Dict)


t1 = (0,1,2,3)
print(t1, type(t1))

print("***********************************************************************")

# Initial Dictionary 
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks', 
		'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'}, 
		'B' : {1 : 'Geeks', 2 : 'Life'}} 
print("Initial Dictionary: ") 
print(Dict) 

# Deleting a Key value 
del Dict[6] 
print("\nDeleting a specific key: ") 
print(Dict) 

# Deleting a Key from 
# Nested Dictionary 
del Dict['A'][2] 
print("\nDeleting a key from Nested Dictionary: ") 
print(Dict) 

# Deleting a Key 
# using pop() 
Dict.pop(5) 
print("\nPopping specific element: ") 
print(Dict) 

# Deleting an arbitrary Key-value pair 
# using popitem() 
Dict.popitem() 
print("\nPops an arbitrary key-value pair: ") 
print(Dict) 

# Deleting entire Dictionary 
Dict.clear() 
print("\nDeleting Entire Dictionary: ") 
print(Dict) 
