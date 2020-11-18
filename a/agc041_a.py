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


n, a, b = LI()
ans = (b-a) // 2 if (b-a) % 2 == 0 else min(a-1, n-b) + 1 + (b-a-1)//2
print(ans)
