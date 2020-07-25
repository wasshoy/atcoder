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
a = LI()
ans = 0
i = 0
while i < n:
    while i+1 < n and a[i] == a[i+1]:
        i += 1
    if i+1 < n and a[i] < a[i+1]:
        while i+1 < n and a[i] <= a[i+1]:
            i += 1
    elif i+1 < n and a[i] > a[i+1]:
        while i+1 < n and a[i] >= a[i+1]:
            i += 1
    ans += 1
    i += 1
print(ans)
