import sys
from collections import defaultdict


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 36


class UnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def get_size(self, x):
        return -self.parents[self.find(x)]

    def check(self, x, y):
        return self.find(x) == self.find(y)

    def get_parent_list(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


n, k, l = LI()
uf_way = UnionFind(n)
for _ in range(k):
    p, q = LI()
    p -= 1
    q -= 1
    uf_way.unite(p, q)

uf_rail = UnionFind(n)
for _ in range(l):
    r, s = LI()
    r -= 1
    s -= 1
    uf_rail.unite(r, s)

d = defaultdict(int)  # d[(i, j)] : グループ i と グループ j に属する頂点の数
for i in range(n):
    # 根の番号 = 属している連結したグループの番号
    rw = uf_way.find(i)
    rr = uf_rail.find(i)
    d[(rw, rr)] += 1  # このグループのどちらにも属する頂点の数

for i in range(n):
    rw = uf_way.find(i)
    rr = uf_rail.find(i)
    print(d[(rw, rr)], end=' ')
