# クラスカル法で最小全域木問題を解くアルゴリズム
# O(E log E)
# 辺をコストが小さい順に見ていき、閉路を作らないように採用していく
# Union Findを使う

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
    sort_e = sorted(edges, key=lambda x: x[2])  # 辺の重み順にソート
    cost = 0
    for e in sort_e:
        s, t, w = e
        if not uf.same(s, t):
            cost += w
            uf.union(s, t)
    return cost


if __name__ == '__main__':
    n = 4
    e = 6
    # we : [頂点1, 頂点2, 重み]
    we = [[0, 1, 2], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 2, 3], [1, 3, 5]]
    uf = UnionFind(4)  # 辺を追加していくグラフ
    res = kruskal(we, uf)
    print(res)
