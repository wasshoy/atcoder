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
if n == 1:
    print(0)
    exit()

base = a[0]
for i in range(1, n):
    if base > a[i]:
        ans += base - a[i]
    else:
        if a[i] > base:
            base = a[i]
print(ans)
