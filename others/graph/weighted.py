from collections import deque
from dataclasses import dataclass


@dataclass
class WeightedGraph:
    n: int
    is_directed: bool = False

    def __post__init__(self, n):
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        """uからvへの(有向な)辺をつなぐ
        Args:
          u(int): 辺が出る頂点
          v(int): 辺が向かう頂点
          w(int): 重み

        Returns:
          なし
        """
        self.graph[u].append([v, w])
        if not self.is_directed:
            self.graph[v].append([u, w])
