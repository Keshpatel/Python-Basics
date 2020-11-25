import datetime


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Keshini', 'Patel', 70000)
emp_2 = Employee('Tom', 'Corey', 60000)

emp1_str = 'Iva-jones-70000'
emp2_str = 'Steve-Smith-30000'
emp3_str = 'kim-doe-90000'

new_emp1_str = Employee.from_string(emp1_str)

print(new_emp1_str.email)
print(new_emp1_str.pay)

my_date = datetime.date(2020, 7, 10)  # returns True
# my_date = datetime.date(2020, 7 , 11)   #  returns False
print(Employee.is_workday(my_date))
