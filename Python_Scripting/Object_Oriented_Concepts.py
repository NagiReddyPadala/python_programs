class MyClass:
    rollNum = 0
    name = "NoName"

class Vector2D:
    x = 0
    y = 0

    def set(self, x, y):
        self.x = x
        self.y = y


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

class Increment:
    __hiddenVar = 0

    def incrementVal(self, val):
        self.__hiddenVar += val
        print(self.__hiddenVar)


class PrintData:
    def __init__(self, x, y):
        self.x = x
        self.y =y
    '''
    def __repr__(self):
        return "repr:" + self.x + " " + self.y
       
    def __str__(self):
        return "str: " + self.x + " " + self.y'''


class X(object): 
	def __init__(self, a): 
		self.num = a 
	def doubleup(self): 
		self.num *= 2

class Y(X): 
	def __init__(self, a): 
		super().__init__(a) 
	def tripleup(self): 
		self.num *= 3

class Bird():
    def intro(self):
        print("This is bird")

    def flight(self):
        print("Some will fly and some won't")

class sparrow(Bird):
    def flight(self):
        print("Sparrow will fly")

class ostrich(Bird):
    def flight(self):
        print("ostrich won't fly")

# Python program to illustrate destructor 
class Employee: 

	# Initializing 
	def __init__(self): 
		print('Employee created.') 

	# Deleting (Calling destructor) 
	def __del__(self): 
		print('Destructor called, Employee deleted.') 

obj = Employee() 
del obj 


        
def main():
    clsObj = MyClass()
    clsObj.rollNum = "75019271"
    clsObj.name = "Nagireddy Padala"
    print("Name is: {}, Roll number is: {}.".format(clsObj.name, clsObj.rollNum))

    vec = Vector2D()
    vec.set(5,6)
    print("X: {}, Y: {}.".format(vec.x, vec.y))

    thePet = Pet("pet", 5)
    jess = Cat("jess", 6)

    print("Is jess is cat ? :" + str(isinstance(jess, Cat)))
    print("Is jess is pet ? :" + str(isinstance(jess, Pet)))
    print("Is thePet is cat ? :" + str(isinstance(thePet, Cat)))
    print("Is thePet is pet ? :" + str(isinstance(thePet, Pet)))

    print(jess.name)
    


    rev = Reverse("NagiReddy")
    for char in rev:
        print (char)

    
    inc = Increment()
    inc.incrementVal(2)
    inc.incrementVal(5)
    print(inc._Increment__hiddenVar)


    data = PrintData("1234", "Hello")
    print(data)
    print([data])

    obj = Y(4) 
    print(obj.num) 

    obj.doubleup() 
    print(obj.num) 

    obj.tripleup() 
    print(obj.num)

    birdObj = Bird()
    birdObj.intro()
    birdObj.flight()

    sparrowObj = sparrow()
    sparrowObj.intro()
    sparrowObj.flight()

    ostrichObj = ostrich()
    ostrichObj.intro()
    ostrichObj.flight()


    obj = Employee() 
    del obj
    number = [1,2,3]
    print(dir(number))

    characters = ["a", "b"]
    print(dir(number))


if __name__ == "__main__":
    main()

