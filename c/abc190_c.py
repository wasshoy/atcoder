import sys
from itertools import product
sys.setrecursionlimit(10**7)


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

n, m = LI()
a = []
b = []
for _ in range(m):
    a_i, b_i = LI()
    a_i -= 1
    b_i -= 1
    a.append(a_i)
    b.append(b_i)

k = I()

ball = [False] * n
cd = LIR(k)
ans = 0
for bits in product((0, 1), repeat=k):
    ball = [False] * n
    res = 0
    for i, choice in enumerate(bits):
        ball[cd[i][choice]-1] = True

    for i in range(m):
        if ball[a[i]] and ball[b[i]]:
            res += 1
    ans = max(ans, res)
print(ans)
