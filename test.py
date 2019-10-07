<<<<<<< HEAD
inputchar = input()
print(inputchar)

inputchar = inputchar.split(",")
print(inputchar)

a = inputchar[0]
b = inputchar[1]

print("a: "+str(a))
print("b: "+str(b))
=======
def gcd(a, b):  # 最大公約数 gcd
    if b != 0:
        return gcd(b, a % b)
    return a


print("gcd(3, 4)")
print(gcd(3, 4))
>>>>>>> euclidean
