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


n, m = LI()
likes = [0] * m
for _ in range(n):
    k, *a = LI()
    for ai in a:
        likes[ai-1] += 1
ans = 0
for like in likes:
    if like == n:
        ans += 1
print(ans)
