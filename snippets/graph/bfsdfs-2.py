# bfsとdfsを行う事ができるグラフクラス
# bfs: O(E)
# dfs: O(V + E)
# 3.7以降対応

from collections import deque
from dataclasses import dataclass


@dataclass
class Graph:
    """有向/無向グラフを作成しbfs/dfsを行うメソッドを持つクラス
    Args:
      n(int): 頂点数
      is_directed(bool): 有向グラフ(True)か無向グラフか(False)
    """

    n: int
    is_directed: bool = False

    def __post__init__(self, n):
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v):
        """uからvへの(有向な)辺をつなぐ
        Args:
          u(int): 辺が出る頂点
          v(int): 辺が向かう頂点

        Returns:
          なし
        """
        self.graph[u].append(v)
        if not self.is_directed:
            self.graph[v].append(u)

    def search(self, start, mode):
        '''開始地点から各頂点まで幅/深さ優先探索を行って得られた距離のリストを返す
        Args:
          start(int): 開始地点となる頂点
          mode(str): 幅優先探索(b)か深さ優先探索(d)を指定

        Returns:
          List[int]: 開始地点からの距離(未到達の場合は-1)
        '''
        dists = [-1] * self.n
        que = deque([start])
        dists[start] = 0
        if mode == 'b':
            # FIFO : 幅優先
            get_v = que.popleft
        else:
            # LIFO : 深さ優先
            get_v = que.pop
        while que:
            now_v = get_v()
            for next_v in self.graph[now_v]:
                if dists[next_v] != -1:
                    continue
                que.append(next_v)
                dists[next_v] = dists[now_v] + 1
        return dists


if __name__ == '__main__':
    g = Graph(5)
