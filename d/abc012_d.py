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


def warshall_floyd(c):
    n = len(c)  # 頂点数
    for k in range(n):
        for i in range(n):
            for j in range(n):
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    return c


n, m = LI()
ans = float('inf')
# costs[i][j] : i から j に直接向かうコスト (inf は直接向かえないことを表す)
costs = [[float('inf') if i != j else 0 for i in range(n)] for j in range(n)]
for _ in range(m):
    a, b, t = LI()
    a, b = a-1, b-1
    costs[a][b] = t
    costs[b][a] = t

min_costs = warshall_floyd(costs)
ans = float('inf')
for i in range(n):
    worst = max(min_costs[i])  # 頂点 i へ向かう最悪の場合のコスト
    ans = min(ans, worst)
print(ans)
