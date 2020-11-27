import sys
from itertools import product


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


class UnionFind():
    def __init__(self, n):
        self.n = n
        # 各要素の親要素 親は -(その集合の要素数)
        self.parents = [-1] * n

    def find(self, x):
        '''要素 x の親要素の番号を返す'''
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        '''要素 x が属する集合と要素 y が属する集合を併合する'''
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        '''要素 x が属する集合の要素数を返す'''
        return -self.parents[self.find(x)]

    def same(self, x, y):
        '''要素 x と要素 y が同じ集合に属するかを返す'''
        return self.find(x) == self.find(y)

    def members(self, x):
        '''要素 x が属する集合の要素をリストを返す'''
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def kruskal(edges, uf):
    cost = 0
    for e in edges:
        s, t, w = e
        if not uf.same(s, t):
            cost += w
            uf.union(s, t)
    return cost


def main():
    n = I()
    a = LIR(n)
    uf = UnionFind(n)
    edges = set()
    for i, j in product(range(n), range(n)):
        if i == j or a[i][j] == -1:
            continue
        edges.add((i, j, a[i][j]))
    edges = sorted(edges, key=lambda x: x[2])  # 辺の重み順にソート

    cost = kruskal(edges, uf)
    print(cost)


main()
