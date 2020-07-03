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
osturi = 1000 - n  # 最大で 999 円 最小で 1 円
m = [500, 100, 50, 10, 5, 1]
ans = 0
for i in m:
    ans += osturi // i
    osturi %= i

print(ans)
