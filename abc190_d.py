import sys
import math
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


n = I()
ans = 0
sqrt = int(math.sqrt(2*n))
for i in range(1, sqrt+1):
    if ((2*n - i*i + i) / (2*i)).is_integer():
        ans += 2
print(ans)
