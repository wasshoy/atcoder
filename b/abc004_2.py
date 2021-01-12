import sys


def input(): return sys.stdin.readline().strip()
def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')
MOD = 10**9 + 7

# 19m AC
c = [input().split() for _ in range(4)]
ans = [['.'] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        ans[i][j] = c[3-i][3-j]

for i in range(4):
    print(*ans[i])
