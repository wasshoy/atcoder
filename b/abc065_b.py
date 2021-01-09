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

# 5m AC
n = I()
a = IR(n)
a = [v-1 for v in a]
now = 0
ans = 0
for _ in range(n):
    now = a[now]
    ans += 1
    if now == 1:
        print(ans)
        exit()
if now == 1:
    print(ans)
else:
    print(-1)
