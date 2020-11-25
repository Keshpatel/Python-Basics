# Object is super class of all the class
class Employee:
    raise_amount = 1.04
    No_Of_Emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@email.com'

        Employee.No_Of_Emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employee = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            print("\nEmployee removed : ", emp.fullname() ,'\n')

    def print_emps(self):
        for emp in self.employees:
            print("Employee-->", emp.fullname())


dev_1 = Developer('Keshini', 'Patel', 70000, 'Python')
dev_2 = Developer('Tom', 'Corey', 60000, 'Python')
dev_3 = Developer('Mili', 'jones', 60000,'Java')


mgr_1 = Manager('Mike', 'smith', 90000, [dev_1])
mag_1 = Manager("Mike", 'smiht', 90000, [dev_3])


print("Manager->\n",mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)
mgr_1.print_emps()

mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)
# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

print('\n', isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(isinstance(mgr_1, Manager))

print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))