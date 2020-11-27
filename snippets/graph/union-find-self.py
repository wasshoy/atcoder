# 自作の Union-Find
class UnionFind:
    def __init__(self, n):
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

    # オプション
    def size(self, x) -> int:  # x が属する集合の要素数
        x = self.r(x)
        return -self.root[x]
