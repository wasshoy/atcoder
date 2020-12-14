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


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        self.parents[root_x] += self.parents[root_y]
        self.parents[root_y] = root_x

    def find(self, x, y):
        return self.root(x) == self.root(y)


n, q = LI()
uf = UnionFind(n)
for _ in range(q):
    p, a, b = LI()
    a -= 1
    b -= 1
    if p == 0:
        uf.unite(a, b)
    else:
        res = 'Yes' if uf.find(a, b) else 'No'
        print(res)
