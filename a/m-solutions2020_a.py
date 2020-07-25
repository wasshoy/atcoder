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

x = I()
if 400 <= x <= 599:
    ans = 8
elif 600 <= x <= 799:
    ans = 7
elif 800 <= x <= 999:
    ans = 6
elif 1000 <= x <= 1199:
    ans = 5
elif 1200 <= x <= 1399:
    ans = 4
elif 1400 <= x <= 1599:
    ans = 3
elif 1600 <= x <= 1799:
    ans = 2
else:
    ans = 1
print(ans)
