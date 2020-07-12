# 26 AC 考察ミス
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
ans = list('123456')
s = n % 30
for i in range(s):
    ans[(i % 5)], ans[(i % 5) + 1] = ans[(i % 5) + 1], ans[(i % 5)]
print(''.join(ans))
