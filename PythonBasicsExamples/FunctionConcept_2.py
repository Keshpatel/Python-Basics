def login(username, password):
    print(username, password)


login("naveen", "test1234")

login(username="KdPatel", password="test@1234")


# *args
def getMarks(*arg):
    for x in arg:
        print(x)


getMarks(10, 23, 79, 55, 86, 80)
getMarks("A", "A+", "B", "B-")


# keyword args:
# **arg

def getStudentMarks(**args):
    for key, value in args.items():
        print("%s= %s" % (key, value))


getStudentMarks(Keshini=80, tim=90, peter=40)
getStudentMarks(key="apple", sellerName="Xeon")

# lanbda function:Annonymous function:
# a function without any name:

cube = lambda x: x * x * x

print(cube(4))

total = lambda marks: marks + 30
print(total(100))
