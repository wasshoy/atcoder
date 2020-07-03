from collections import deque
import sys


def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))


INF = float('inf')


class Graph:
    """無向(/有向)グラフに対してbfsとdfsを行い任意の頂点からの距離を算出する
    """

    def __init__(self, n, is_directed=False):
        """
        :param n: 頂点数
        :param is_directed: 有向グラフ(True)か無向グラフか(False)
        """
        self.graph = [[] for _ in range(n)]
        self.is_directed = is_directed

    def add_edge(self, u, v):
        """頂点uから頂点vに辺を作る
        無向グラフの場合、uからvの方向の辺のみを記録する
        """
        self.graph[u].append(v)
        if not self.is_directed:
            self.graph[v].append(u)

    def bfs(self, start):
        """幅優先探索を行い始点から各頂点までの距離の配列を返す
        """
        distances = [INF] * len(self.graph)
        queue = deque([start])
        distances[start] = 0
        # ans = [0] * len(self.graph)

        while queue:
            now = queue.popleft()
            for to in self.graph[now]:
                if distances[to] != INF:
                    continue
                queue.append(to)
                distances[to] = distances[now] + 1
        return distances

    def dfs(self, start):
        """深さ優先探索を行い始点から各頂点までの距離の配列を返す
        """
        distances = [INF] * len(self.graph)
        queue = deque([start])
        distances[start] = 0

        while queue:
            now = queue.pop()
            for to in self.graph[now]:
                if distances[to] != INF:
                    continue
                queue.append(to)
                # 前の頂点からこの頂点に対する道標を建てる
                distances[to] = distances[now] + 1
        return distances


def main():
    n, m = LI()
    g = Graph(n)
    for _ in range(m):
        a, b = LI()
        a, b = a - 1, b - 1
        g.add_edge(a, b)


if __name__ == '__main__':
    main()
