# 24
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
d = set(LI())
# 最小金額から条件を満たすまで増やしていく
while True:
    if all(int(j) not in d for j in str(n)):  # 全ての桁の数字が d に属さない
        print(n)
        exit()
    n += 1
