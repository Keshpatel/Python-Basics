class Employee:

    #hidden data member of employee class
    __salary = 1000

e1 = Employee()
# print(e1.__salary) -- This is not the write way of accessing hidden private variable

# access private hidden variable by tricky syntax:
print(e1._Employee__salary)



