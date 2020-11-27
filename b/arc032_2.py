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

# 23


class UnionFind:
    def __init__(self, n):
        self.root = [-1] * n  # 各要素の親 親自身は -i (i は連結成分の要素数)

    def r(self, x):  # x の 親を返す
        if self.root[x] < 0:  # 自身が親
            return x
        else:  # 再帰的に親を辿る
            self.root[x] = self.r(self.root[x])
            return self.root[x]

    def unite(self, x, y):  # x と y を連結
        x = self.r(x)
        y = self.r(y)
        if x == y:
            return  # 何もしない
        self.root[x] += self.root[y]
        self.root[y] = x


N, M = LI()
E = []
uf = UnionFind(N)
for _ in range(M):
    a, b = LI()
    a, b = a-1, b-1
    uf.unite(a, b)

# 連結成分の個数 - 1 = 建設すべき道路の最小数
ans = 0
for r in uf.root:
    if r < 0:
        ans += 1
print(ans-1)
