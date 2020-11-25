# Python Object-Oriented Programming

class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Keshini', 'Patel', 70000)
emp_2 = Employee('Tom','Corey',60000)

print(emp_1.email)
print(emp_2.email)

# using class name and passing Instance of the class
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

# Using instance and no need to pass anything
emp_1.fullname()
emp_2.fullname()





