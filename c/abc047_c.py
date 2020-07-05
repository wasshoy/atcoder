# 32m AC
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

s = S()
n = len(s)
ans = 0
for i in range(n - 1):
    if s[i] != s[i + 1]:
        ans += 1
print(ans)
