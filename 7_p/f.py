import sys

sys.setrecursionlimit(100000)


def f(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return f(m-1, 1)
    else:
        return f(m-1, f(m, n-1))


print(f(4, 6))
