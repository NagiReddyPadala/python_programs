import datetime
class Employee:
    raiseAmount = 1.05
    num_of_emps = 0

    def __init__(self, fisrtName, lastName, salary):
        self.firstName = fisrtName
        self.lastName = lastName
        self.salary = salary
        self.mailId = fisrtName + lastName + '@company.com'
        #self.raiseAmount = 1.06

        Employee.num_of_emps += 1

    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)


    def applyRaise(self):
        self.salary = int(self.salary) * self.raiseAmount

    @classmethod
    def fromSrting(cls, cls_str):
        first, last, pay = cls_str.split('-')
        return cls(first, last, pay)

    @classmethod
    def set_raise_amont(cls, raise_amount):
        cls.raiseAmount = raise_amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print(Employee.num_of_emps)
#emp1= Employee("Nagireddy", "Padala", 100000)
cls_str = "Nagireddy-Padala-100000"
emp1= Employee.fromSrting(cls_str)
emp2 = Employee("Madhuri", "Goluguri", 200000)

# print(emp1)
# print(emp1.fullName())
# print(emp1.salary)
# print(emp1.applyRaise())
# print(emp1.salary)
#
#
# print(emp2)
#

Employee.set_raise_amont(1.07)
print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(emp1.applyRaise())
print(emp1.salary)
print(emp1.__dict__)

#Employee.raiseAmount = 1.06
emp1.raiseAmount = 1.04
print(emp1.__dict__)

print(Employee.raiseAmount)
print(emp1.raiseAmount)
print(emp2.raiseAmount)
print(emp1.applyRaise())
print(emp1.salary)


#print(emp1.__dict__)
print(Employee.num_of_emps)
print(emp1.fullName())
print(emp2.fullName())
print(Employee.fullName(emp1))

mydate = datetime.date(2020, 2, 8)
print(Employee.is_workday(mydate))