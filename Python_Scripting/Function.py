def myFun(x):
    print(id(x))
    x[0] = 10


lst = [1,2,3,4,5,6]
myFun(lst)
print(id(lst))
print(lst)


def myFun(x):
    x = [10]


lst = [1,2,3,4,5,6]
myFun(lst)
print(lst)


def myFun(x):
    #x = 20
    print(id(x))
    print(x)

x = 10
myFun(x)
print(id(x))
print(x) 


# Python code to illustrate cube of a number 
# using labmda function 
	
cube = lambda x: x*x*x 
print(cube(7))


# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
	return text.upper() 

print (shout('Hello')) 

yell = shout 

print (yell('Hello')) 
#print(id(shout()))
print(id(yell))


def caps(text):
    return text.upper()

def small(text):
    return text.lower()

def callFunc(func):
    print(func("Hello, I AM Nagireddy"))

callFunc(caps)
callFunc(small)
    
    
    
def welcomeMessage(str):
    def welcome():
        return "Welcome to "
    return welcome() + str

def returnStr(str):
    return str

print(welcomeMessage(returnStr("Nagi")))


def welcomeMessage(fun):
    def welcome(str):
        return "Welcome to " + fun(str)
    return welcome

@welcomeMessage
def returnStr(str):
    return str




def increment(value):
    return value+1

incrementTheVal = increment
print(id(increment))
print(id(incrementTheVal))
print(incrementTheVal(5))


def plus_one(val):
    def addOne(val):
        return val+1
    return addOne(val)

print(plus_one(4))


def plus_one(val):
    return val+1

def minus_one(val):
    return val-1

def function_call(func, val):
    return func(val)

print(function_call(plus_one,1))
print(function_call(minus_one,10))


def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello)
print(hello())


def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")



def upper_case_decorator(func):
    def wrapper():
        myFunc = func()
        return myFunc.upper()

    return wrapper

def split_str(func):
    def wrapper():
        myFunc = func()
        return myFunc.split()
    return wrapper

@split_str
@upper_case_decorator
def say_hi():
    return "Hey Madhu, I love you."

print("**", say_hi())
#decorate = upper_case_decorator(say_hi)
#print(decorate())


def myDecoratorFunc(func):
    def myWrapper(arg1, arg2):
        print(func(arg1, arg2))
        return "State is {0} and capital is {1}".format(arg1, arg2)

    return myWrapper

@myDecoratorFunc
def printStateDetails(arg1,arg2):
    return "State and capital details are: "

print(printStateDetails("Andhra Pradesh", "Visakhapatnam")) 




def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

print(function_with_no_argument())

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

print(function_with_arguments(1,2,3))



@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

print(function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti"))




def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3) :
            "This is the wrapper"
            print("The wrapper can access all the variables\n"
                  "\t- from the decorator maker: {0} {1} {2}\n"
                  "\t- from the function call: {3} {4} {5}\n"
                  "and pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,decorator_arg3,
                          function_arg1, function_arg2,function_arg3))
            return func(function_arg1, function_arg2,function_arg3)

        return wrapper

    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
    print("This is the decorated function and it only knows about its arguments: {0}"
           " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

decorated_function_with_arguments(pandas, "Science", "Tools")
print(decorated_function_with_arguments.__name__)
print(decorated_function_with_arguments.__doc__)



class Helper: 
    def __init__(self): 
        '''The helper class is initialized'''
  
    def print_help(self): 
        '''Returns the help description'''
        print('helper description') 
  
help(Helper) 
help(Helper.print_help) 



# Python program to understand range 
# this creates a list of 0 to 5 
# integers 

demo = range(6) 

# print the demo 
print(demo) 

# it will generate error 
#print(next(demo)) 


# Python program to understand range 

# creates an iterator 
demo = iter(range(6)) 

# print iterator 
print(demo) 

# use next 
print(next(demo)) 
print(next(demo)) 
print(next(demo)) 



# Simple recursive program to find factorial 
def facto(num): 
    if num == 1: 
        return 1
    else: 
        return num * facto(num-1) 
          
  
print(facto(5))
