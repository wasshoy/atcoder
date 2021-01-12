import sys


def input(): return sys.stdin.readline().strip()
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

n = I()
# ニコニコ数は全て25を約数に持つ
# 25はニコニコ数なのである整数mが25を約数に持つなら、25以外のニコニコ数を約数に保つ場合でも網羅できる
ans = n // 25
print(ans)
