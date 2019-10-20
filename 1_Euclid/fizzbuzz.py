fizz = input("fizz: ")
buzz = input("buzz: ")
a = int(input("num1: "))
b = int(input("num2: "))

for i in range(100):
    if(i % a):
        print(fizz)
        if(i % b):
            print(fizz+buzz)
    elif(i % b):
        print(buzz)
