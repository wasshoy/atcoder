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

sys.setrecursionlimit(10**7)

# 46
n = I()
a = LI()
ans = 0
r = 1
for l in range(n):
    while r < n and (r <= l or a[r-1] < a[r]):
        r += 1
    ans += r - l
    if l == r:
        r += 1
print(ans)
