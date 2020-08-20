# 6m AC
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

c = S()
n = len(c)
ans = ''
for i in range(n-1):
    if c[i] == ' ' and c[i+1] != ' ':
        ans += ','
    elif c[i] != ' ':
        ans += c[i]
    else:
        continue
ans += c[-1]
print(ans)
