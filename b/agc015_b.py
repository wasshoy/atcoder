# 012
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
ans += (n - 1) + (n - 1)
for i in range(1, n - 1):
    if s[i] == 'U':
        ans += n-i-1 + 2*i
    else:
        ans += 2*(n-i-1) + i
print(ans)
