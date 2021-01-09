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


# 12m AC
q, h, s, d = LI()
n = I()
if n % 2 == 0:
    ans = min(d*(n//2), s*n, h*n*2, q*n*4)
    print(ans)
else:
    n -= 1
    ans = min(d*(n//2), s*n, h*n*2, q*n*4)
    ans += min(s, h*2, q*4)
    print(ans)
