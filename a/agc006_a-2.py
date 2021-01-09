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
s = S()
t = S()
# 全探索
ans = 2 * n
res = s + t
for i in range(n+1):
    res = s + t[i:]
    if res[:n] == s and res[-n:] == t:
        ans = min(ans, 2*n - i)
print(ans)
