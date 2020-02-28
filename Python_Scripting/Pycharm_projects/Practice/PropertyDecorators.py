class Employee:

    def __init__(self, fisrtName, lastName):
        self.firstName = fisrtName
        self.lastName = lastName
        #self.mailId = fisrtName + lastName + '@company.com'
        #self.raiseAmount = 1.06
        msg = "Hello"

    @property
    def mailId(self):
        return "{}.{}@company.com".format(self.firstName, self.lastName)

    @property
    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last

    '''
    @fullName.getter
    def fullName(self):
        return "Testing getter"
    '''

    @fullName.deleter
    def fullName(self):
        print("Testing deleter")
        self.firstName = None
        self.lastName = None


emp1 = Employee("Nagireddy", "Padala")
print(emp1.mailId)
print(emp1.fullName)

emp1.fullName = "Madhuri Padala"
print(emp1.mailId)
print(emp1.fullName)


del emp1.fullName
print(emp1.fullName)
print(emp1.mailId)
