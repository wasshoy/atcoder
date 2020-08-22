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


n = I()
w = LI()
t = float('inf')
s_1 = 0
s_2 = sum(w)
for i in range(n):
    s_1 += w[i]
    s_2 -= w[i]
    t = min(t, abs(s_1 - s_2))
print(t)
