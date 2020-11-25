name = "Alex"
for i in name:
    print(i)
    if(i == 'x'):
        break

name = "Alex"
for i in name:
    print(i)
    if(i == 'x'):
        continue


str = ["Python", "java", "C Sharp", "Dot Net"]
for l in range(len(str)):
    print(str[l])
    if(str[l] == "java"):
        print("hey I found Java!!")
        break


lang = ["Hindi", "English", "Spanish","German", "Chinese"]
flag = False
for index in range(len(lang)):
    print("Spanish is the 2ed poplular language in the world")
    flag = True
    break

if(flag):
    print("I want to learn Spanish")




