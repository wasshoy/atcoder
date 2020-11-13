from itertools import product
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


s_n = input()
l_n = list(s_n)
k = len(s_n)
n = int(s_n)
ans = INF
for bits in product((False, True), repeat=k):
    num = [int(i) for i, bit in zip(l_n, bits) if bit]
    d = k - len(num)
    if len(num) != 0 and sum(num) % 3 == 0:
        ans = min(ans, d)
if ans == INF:
    ans = -1
print(ans)
