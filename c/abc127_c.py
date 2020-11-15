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
left, right = LI()
for _ in range(m-1):
    l, r = LI()
    if left < l:
        left = l
    if r < right:
        right = r
ans = right - left + 1 if right - left >= 0 else 0
print(ans)
