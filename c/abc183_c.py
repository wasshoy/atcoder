from itertools import permutations
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


n, k = LI()
t = LIR(n)
ans = 0
for p in permutations(range(1, n)):
    # print(p)
    time = 0
    now = 0
    for j in p:
        time += t[now][j]
        now = j
    time += t[now][0]
    if time == k:
        ans += 1
print(ans)
