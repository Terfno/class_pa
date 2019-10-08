import time


def getTime():  # 現在時刻の取得関数
    return time.time()


def gcd(a, b):  # 最大公約数 gcd
    if b != 0:
        return gcd(b, a % b)
    return a


def lcm(ab, g):  # 最小公倍数 lcm
    return ab/g


def main():  # 最大公約数と最小公倍数を計算し、その結果と計算時間表示する
    # 時間計測
    startTime = getTime()

    # 入力
    inputnum = input("input 2 Integer: ").split(",")
    a = int(inputnum[0])
    b = int(inputnum[1])

    # 計算
    g = gcd(a, b)
    l = lcm(a*b, g)

    # 表示
    print('{:.100g}'.format(g))
    print('{:.100g}'.format(l))
    print("calc time: " + str(getTime() - startTime) + "[ms]")


main()
