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

# 30m AC
# 座標圧縮を行う問題
n = I()
a = IR(n)
na = list(set(a))
na.sort()
d = {}
v = 0
for i in na:
    d[i] = v
    v += 1

b = [0] * n
for i, ai in enumerate(a):
    b[i] = d[ai]
print(*b, sep='\n')
