class Employee:

    raise_amount = 1.04
    No_Of_Emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

        Employee.No_Of_Emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print("Total Employee: " ,Employee.No_Of_Emp)

emp_1 = Employee('Keshini', 'Patel', 70000)
emp_2 = Employee('Tom', 'Corey', 60000)

# print(emp_1.__dict__)
# print(Employee.__dict__)

emp_1.raise_amount = 1.05
print(emp_1.__dict__)

print(Employee.raise_amount)

print(emp_1.raise_amount)
print(emp_2.raise_amount)

print("Total Employee: " , Employee.No_Of_Emp)