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


n, k = LI()
a = LI()
base = 1
for i in range(k, n):
    rate = a[i] / a[i-k]
    if rate > 1:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)
