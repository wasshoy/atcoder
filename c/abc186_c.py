import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


def nshin(x, n):
    dum = x
    res = ''
    while dum > 0:
        res = str(dum % n) + res
        dum //= n
    return res


n = I()
ans = n
for i in range(1, n+1):
    # print(i, nshin(i, 8))
    if '7' in str(i) or '7' in str(nshin(i, 8)):
        ans -= 1
print(ans)
