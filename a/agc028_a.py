# 02
import sys
import math


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
s = S()
t = S()

gcd = math.gcd(n, m)
lcm = n * m // gcd
i_s = n // gcd
i_t = m // gcd
for i in range(gcd):
    if s[i*i_s] != t[i*i_t]:
        print(-1)
        exit()
print(lcm)
