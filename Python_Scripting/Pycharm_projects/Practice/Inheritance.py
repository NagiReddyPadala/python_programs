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

class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self, fisrtName, lastName, salary, prog_lang):
        self.prog_lang = prog_lang
        super().__init__(fisrtName, lastName, salary)

    def fullName(self):
        return "{} - {}".format(self.firstName, self.lastName)

class Manager(Employee):
    def __init__(self, fisrtName, lastName, salary, employees = None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        super().__init__(fisrtName, lastName, salary)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullName())

#help(Developer)

print(Employee.num_of_emps)
dev1= Developer("Nagireddy", "Padala", 100000, "python")
dev2 = Developer("Madhuri", "Goluguri", 200000, "java")

print(Employee.num_of_emps)
print(dev1.salary)
dev1.applyRaise()
print(dev1.salary)
print(dev1.prog_lang)
print(dev1.fullName())
#emp2 = Employee("Madhuri", "Goluguri", 200000)


manager = Manager("Manager", "Manager", 250000, [dev1])

print(manager.fullName())
print(manager.mailId)
print(manager.print_emp())
manager.add_emp(dev2)
print(manager.print_emp())
manager.remove_emp(dev1)
print(manager.print_emp())

print(isinstance(manager, Developer))
print(isinstance(manager, Employee))
print(isinstance(dev1, Employee))
#print(issubclass(manager, Employee))
#print(issubclass(dev1, Employee))

print("-----------------")

