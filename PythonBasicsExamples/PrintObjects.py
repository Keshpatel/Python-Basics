# string representation of class object:
# Object printing concept:

class Test:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "x:%s y:%s" % (self.x, self.y)

    def __str__(self):
        return "value of a is %s and y is %s" %(self.x, self.y)


# Test Code:
# if there are both method then str will get consider .
# if there is no str method then it will call repr method
# if both str and repr both method is not available then it will give an error .
#
t= Test(10, 20)
print(t)