# 幅優先と深さ優先を行うクラス
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
    graph: list = [[] for _ in range(n)]

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

    def bfs(self, start):
        """開始地点から各頂点までの距離のリストを返す
        Args:
          start(int):開始地点となる頂点

        Returns:
          List[int]: 開始地点からの距離(未到達の場合は-1)
            """
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
            get_v = que.popleft
        else:
            get_v = que.pop
        while que:
            now_v = get_v()
            for next_v in self.graph[now_v]:
                if dists[next_v] != -1:
                    continue
                que.append(next_v)
                dists[next_v] = dists[now_v] + 1
        return dists
