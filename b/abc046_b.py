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
if n == 1:
    print(k)
    exit()
ans = k  # 一番左の1個は何色でも良い
for _ in range(n-1):  # 残りの n-1個は前に選んだ色以外の色
    ans *= k-1
print(ans)
