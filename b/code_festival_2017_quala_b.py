# 03
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


N, M, K = LI()

for i in range(N+1):
    for j in range(M+1):
        if i*(M-j) + j*(N-i) == K:
            print('Yes')
            exit()

print('No')
