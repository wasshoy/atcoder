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

# 47


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n  # 各要素の親 親自身は -i (i は集合の要素数)

    def r(self, x):  # x の 親を返す
        if self.root[x] < 0:  # 自身が親
            return x
        else:  # 再帰的に親を辿る
            self.root[x] = self.r(self.root[x])
            return self.root[x]

    def union(self, x, y):  # x と y を連結
        x = self.r(x)
        y = self.r(y)
        if x == y:
            return  # 何もしない
        self.root[x] += self.root[y]
        self.root[y] = x

    def find(self, x, y) -> bool:  # x と y は同じ集合に属しているか
        return self.root[x] == self.root[y]

    def size(self, x) -> int:  # x が属する集合の要素数
        x = self.r(x)
        return -self.root[x]

    def members(self, x):
        '''要素 x が属する集合の要素をリストを返す'''
        root = self.r(x)
        return [i for i in range(self.n) if self.r(i) == root]

    def roots(self):  # 全ての親を返す
        return [i for i, x in enumerate(self.root) if x < 0]

    def all_group_members(self):  # 親とそれに属するグループを返す
        return {r: self.members(r) for r in self.roots()}


n, m = LI()
uf = UnionFind(n)
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = LI()
    u -= 1
    v -= 1
    uf.union(u, v)
    edges[u].append(v)
    edges[v].append(u)

ans = 0
# 連結成分のグループごとに木かどうか判定
for parent, mems in uf.all_group_members().items():
    e_cnt = 0  # 連結成分の辺の数
    for v in mems:
        e_cnt += len(edges[v])
    e_cnt //= 2
    v_cnt = len(mems)
    if e_cnt <= v_cnt - 1:
        ans += 1
print(ans)
