# 1WA 1subミス 35m AC
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
if x <= 6:
    ans = 1
elif x <= 11:
    ans = 2
else:
    ans = (x // 11) * 2
    if x % 11 == 0:
        pass
    elif x % 11 <= 6:
        ans += 1
    elif x % 11 <= 10:
        ans += 2
print(ans)
