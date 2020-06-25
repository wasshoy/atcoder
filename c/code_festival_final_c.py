import sys

sys.setrecursionlimit(10 ** 7)


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def f(n):
    ns = list(map(int, str(n)))
    res = 0
    for i, elem in enumerate(ns[::-1]):
        res += elem * (n ** i)
    return res


def is_g(n, k):
    ks = list(map(int, str(k)))
    for i, elem in enumerate(ks[::-1]):
        # print(i, elem)
        n -= elem * (k ** i)
        # print(n)
    if n == 0:
        return True
    return False


def main():
    a = I()
    ans = -1
    for k in range(10, 10 ** 6):
        if is_g(a, k):
            ans = k
            break
    print(ans)


main()
