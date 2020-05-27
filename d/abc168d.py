from collections import deque
import sys


INF = float('inf')


def I(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))


class Graph:
    def __init__(self, n, is_directed=False):
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
        ans = [0] * len(self.graph)

        while queue:
            now = queue.popleft()
            for to in self.graph[now]:
                if distances[to] != INF:
                    continue
                queue.append(to)
                # 現在の頂点に隣接する頂点の道標を現在の頂点に向ける
                ans[to] = now
                distances[to] = distances[now] + 1
        return distances, ans


def main():
    n, m = LI()
    g = Graph(n)
    for _ in range(m):
        a, b = LI()
        a, b = a - 1, b - 1
        g.add_edge(a, b)

    bfs_res, ans = g.bfs(0)
    for d in bfs_res:
        if d == INF:
            print('No')
            return

    print('Yes')
    print(*map(lambda x: x + 1, ans[1:]), sep='\n')


if __name__ == '__main__':
    main()
