def test():
    print("Hello World")


# calling the function test()
test()


def abc(a):
    print(a + 10)


# calling the function abc()
abc(10)


# Optional/default parameter:
def getcountryname(name="India"):
    print(name)


getcountryname("Canada")
getcountryname("UK")
getcountryname(100)


# Pass a list to a function:
def getnames(list):
    for x in list:
        print(x)


names = ["Java", "Python", "DoTNET", "Ruby"]
getnames(names)


# function with return :
def sum(a, b):
    c = a + b
    return c

s1 = sum(10, 20)
print(s1)


def getCapitalName(countryName):
    if countryName == "Canada":
        return "Ottawa"
    elif countryName == "USA":
        return "Washington DC"


print(getCapitalName("Canada"))
print(getCapitalName("USA"))


def launchBrowser(browserName):
    if browserName == 'chrome':
        print("launching google chrome")
    elif browserName == "firefox":
        print("launching firefox chrome")
    else:
        print("No browser is defined")


launchBrowser("chrome")
launchBrowser("firefox")
launchBrowser("safari")


# Recursion in Python :
# A function is calling itself

# WAP to get factorial of given number:
# fact(4) = 4 * 3 * 2 * 1 = 24
# fact(5) = 5 * 4 * 3 * 2 * 1 = 120

def facto(num):
    if num > 1:
        num = num * facto(num - 1)
        return num
    return num


# Calling Facto()
print(facto(4))
print(facto(5))


def login(username, password):
    print("login with %s and %s " % (username, password))
