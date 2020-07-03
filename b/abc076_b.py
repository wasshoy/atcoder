# bit 全探索 の解法
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


n = I()
k = I()
ans = INF
for i in range(2 ** n):
    res = 1
    for j in range(n):
        if i >> j & 1:
            res *= 2
        else:
            res += k
    ans = min(ans, res)
print(ans)
