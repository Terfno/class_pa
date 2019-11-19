# 与えられたnに対して原始根の個数を返す
def gcd(a, b):  # 最大公約数 gcd
    if b != 0:
        return gcd(b, a % b)
    return a


def phi(n):
    count = 0

    for i in range(1, n):
        if(gcd(i, n) == 1):
            count = count + 1

    return count


def main():
    inputN = input("inpute N as integer: ")
    n = int(inputN)
    count = phi(n)
    print(count)


main()
