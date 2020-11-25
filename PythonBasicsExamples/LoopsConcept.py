# While loop:
count = 0
while(count<3):
    print("Hello World")
    print(count)
    count = count + 1

print("__________________")

num = 0
while(num<3):
    print("Hello Python")
    num = num+1
else:
    print("I am liking Python")

# for loop:
name = ["java", "python", "dot net", "C#"]
for i in name:
    print(i)

str = "I love Python"
for i in str:
    print(i)

list =["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])

# for loop with else:
Country_List = ["India", "USA", "UK", "Germany"]
for index in range(len(Country_List)):
    print(Country_List[index])
else:
    print("CountryList is over")

City_List = ["Banglore", "NY", "LA", "Berlin"]
for index in range(2):
    print(City_List[index])
else:
    print("City List is over")

print("________________")

# Nested For ... Loop
for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()










