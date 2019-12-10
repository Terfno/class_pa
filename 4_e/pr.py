def is_primitive_root(i, n):
    k = n_order(i, n)
    return k == n - 1 # if(k == n-1):true みたいな


def n_order(i, n):
    k = 1
    l = i
    while l != 1:
        l = (l*i) % n
        k += 1
    return k


def primitive_root(n):
    k = 1
    flag = False
    while not flag:
        l = k
        i = 2
        while l != 1:
            l = (l*k) % n
            i += 1
        if i == n:
            flag = True
        else:
            k += 1
    return k


def main():
    n = 11
    # 原始根であるか調べる
    for i in range(1, n):
        if is_primitive_root(i, n):
            print('{0}は{1}の原始根です'.format(i, n))
        else:
            print('{0}は{1}の原始根ではありません'.format(i, n))
    print()
    # 原始根を求める
    print('{0}の原始根は{1}です'.format(n, primitive_root(n)))
    print()
    # 位数を求める
    for i in range(1, n):
        print('{0}を法とする{1}の位数は{2}です'.format(n, i, n_order(i, n)))


main()
