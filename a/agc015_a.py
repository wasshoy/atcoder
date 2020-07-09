# 10m AC (1WA)
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


n, a, b = LI()

min_s = a * (n - 1) + b
max_s = a + (n - 1) * b
ans = max_s - min_s + 1
if ans < 0:
    ans = 0
print(ans)
