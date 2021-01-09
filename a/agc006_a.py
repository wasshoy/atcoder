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

# 13m AC
n = I()
s = S()
t = S()
# s と t の一致部分を調べる
max_length = 0
for i in reversed(range(n)):
    for j in range(n+1):
        if s[i:] == t[:j]:
            max_length = max(max_length, j)

ans = 2*n - max_length
print(ans)
