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

# 58
x_a, y_a, x_b, y_b, x_c, y_c = LI()
# 1点を原点に移動
ans = abs((x_a-x_c)*(y_b-y_c) - (x_b-x_c)*(y_a-y_c)) / 2
print(ans)
