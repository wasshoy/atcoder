# 58
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
h = LI()
ans = 0
while True:
    if max(h) == 0:
        break
    i = 0
    while i < n:
        if h[i] == 0:
            i += 1
        else:
            ans += 1
            while i < n and h[i] > 0:
                h[i] -= 1
                i += 1
print(ans)
