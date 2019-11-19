def gcd(a, b):  # 最大公約数 gcd
    if b != 0:
        return gcd(b, a % b)
    return a


def main():
    print(gcd(6, 2))

main()