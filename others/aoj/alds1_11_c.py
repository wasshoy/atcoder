from collections import deque
import sys


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())


class Graph:
    def __init__(self, n, is_directed=False):
        """
        :param n: 頂点数
        :param is_directed: 有向グラフ(True)か無向グラフか(False)
        """
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.is_directed = is_directed

    def add_edge(self, u, v):
        """uからvへの(有向な)辺をつなぐ"""
        self.graph[u].append(v)
        if not self.is_directed:
            self.graph[v].append(u)

    def bfs(self, start):
        """開始地点から各頂点までの最短距離のリストを返す"""
        dists = [-1] * self.n
        que = deque([start])
        dists[start] = 0

        while que:
            now_v = que.popleft()
            for next_v in self.graph[now_v]:
                if dists[next_v] != -1:
                    continue
                que.append(next_v)
                dists[next_v] = dists[now_v] + 1
        return dists


n = I()
g = Graph(n, is_directed=True)
for _ in range(n):
    u, k, *v = LI()
    u -= 1
    # print(u, k, v)
    if v == []:
        continue
    for vi in v:
        vi -= 1
        g.add_edge(u, vi)
# print(g.graph)
res = g.bfs(0)
for i in range(n):
    print(i + 1, res[i])
