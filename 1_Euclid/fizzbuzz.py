fizz = input("fizz: ")
buzz = input("buzz: ")
a = int(input("num1 int: "))
b = int(input("num2 int: "))
maxnum = int(input("max int: "))

for i in range(maxnum):
    if(i % a):
        print(fizz)
        if(i % b):
            print(fizz+buzz)
    elif(i % b):
        print(buzz)
