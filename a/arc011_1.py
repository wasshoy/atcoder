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

# 20m AC
m, n, N = LI()
ans = N
now = N
rest = 0

while True:
    if now == 0:
        if rest >= m:
            now = rest
            rest = 0
        else:
            break
    rest += now % m
    now = (now//m) * n
    ans += now
print(ans)
