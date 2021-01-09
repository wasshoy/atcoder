import sys
import math


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')
MOD = 10**9 + 7

# 37m AC
n = I()
c = []
s = []
f = []
for _ in range(n-1):
    ci, si, fi = LI()
    c.append(ci)
    s.append(si)
    f.append(fi)

ans = []
for i in range(n):
    t = 0
    for j in range(i, n-1):
        if t < s[j]:
            t = s[j]
        else:
            t = math.ceil(t / f[j]) * f[j]
        t += c[j]
    ans.append(t)
print(*ans, sep='\n')
