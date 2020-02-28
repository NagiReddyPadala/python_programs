import datetime

class Employee:
    raise_amount = 1.05

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    @property
    def mail_id(self):
        return self.first_name.lower() + '.' + self.last_name.lower() + '@company.com'

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, full_name):
        first, last = full_name.split(' ')
        self.first_name = first
        self.last_name = last

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def set_raise_amount(cls, raise_amount):
        cls.raise_amount = raise_amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        year, month, date = day.split("-")
        day1 = datetime.date(int(year), int(month), int(date))
        if day1.weekday() == 5 or day1.weekday() == 6:
            return False
        return True

    def __add__(self, otherEmp):
        return self.salary + otherEmp.salary

    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.first_name, self.last_name, str(self.salary))

    def __str__(self):
        return "{} - {}".format(self.full_name, self.mail_id)

    def __len__(self):
        return len(self.full_name)


class Developer(Employee):
    def __init__(self, first_name, last_name, salary, languages):
        super().__init__(first_name, last_name, salary)
        self.languages = languages

    @property
    def full_name(self):
        return self.first_name + '-' + self.last_name


class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees = None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-----> ", emp.full_name)


emp1 = Employee('Nagireddy', 'Padala', '10000')
emp2 = Employee('Madhuri', 'Goluguri', '10000')

print(emp1.first_name)
print(emp1.last_name)
print(emp1.salary)
print(emp1.mail_id)
print(emp1.full_name)
#emp1.apply_raise()
#print(emp1.salary)

print("**********************")

print(emp2.first_name)
print(emp2.last_name)
print(emp2.salary)
print(emp2.mail_id)
print(emp2.full_name)
#emp2.apply_raise()
#print(emp2.salary)

print("**********************")
Employee.set_raise_amount(1.20)

emp1.apply_raise()
emp2.set_raise_amount(1.30)
emp2.apply_raise()

print(emp1.salary)
print(emp2.salary)


# emp1.first_name = 'Madhuri'
# emp1.last_name = 'Goluguri'

# print(emp1.first_name)
# print(emp1.last_name)
# print(emp1.salary)
# print(emp1.mail_id)
# print(emp1.full_name)
#
# emp1.full_name = "Madhu Padala"
# print(emp1.full_name)

print("##########################################")

emp3 = Employee.from_string("Anitha-Padala-10000")
print(emp3.first_name)
print(emp3.last_name)
print(emp3.salary)
print(emp3.mail_id)
print(emp3.full_name)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(Employee.is_workday("2020-02-16"))
#print(Employee.apply_raise(emp1))


print("#######################################")
dev1 = Developer("Nagireddy", "Padala", "20000", ['Python', 'Java'])
dev2 = Developer("Madhuri", "Padala", "20000", ['JS', 'Java'])
dev3 = Developer("Anitha", "Padala", "20000", ['C++', 'Java'])

mang1 = Manager("Nagireddy", "Padala", "20000", [dev1])

print(dev1.first_name)
print(dev1.last_name)
print(dev1.salary)
print(dev1.mail_id)
print(dev1.full_name)
print(dev1.languages)

mang1.print_emp()
print("###############################")

mang1.add_emp(dev2)
mang1.print_emp()

print("###############################")
mang1.add_emp(dev3)
mang1.print_emp()

print("###############################")
mang1.remove_emp(dev1)
mang1.print_emp()

print(emp1+emp2)

print(emp1)
print(emp2)


print(len(emp1))

print(dir(dev1))
print(help(dev1))