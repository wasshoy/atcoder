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
MOD = 10**9 + 7

# 7WA + 30m AC
n = I()
d = LIR(n)
now_t = 0
now_x = 0
now_y = 0
is_ok = True
for (t, x, y) in d:
    col_t = t - now_t
    md = abs(x - now_x) + abs(y - now_y)
    if not(col_t % 2 == md % 2 and md <= col_t):
        print('No')
        exit()
    now_t = t
    now_x = x
    now_y = y

print('Yes')
