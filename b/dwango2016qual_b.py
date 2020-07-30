# 13m AC
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
k = LI()
l = [0] * n
l[0] = k[0]
for i in range(n - 2):
    if k[i] <= k[i+1]:
        l[i+1] = k[i]
    else:
        l[i+1] = k[i+1]
l[-1] = k[-1]
print(*l, sep=' ')
