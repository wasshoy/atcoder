from collections import defaultdict
from copy import deepcopy
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


def dfs(graph, v, visited):
    visited.add(v)
    for nv in graph[v]:
        if nv not in visited:
            dfs(graph, nv, visited)
    return visited


def is_connected(graph, nodes_cnt):
    visited = dfs(graph, 1, set())
    # 頂点1から一気に全頂点に訪問できているか
    if len(visited) == nodes_cnt:
        return True
    else:
        return False


n, m = LI()
edges = [LI() for _ in range(m)]
g = defaultdict(set)
for u, v in edges:
    g[u].add(v)
    g[v].add(u)

ans = 0
# 辺を一本ずつ除いていく
for u, v in edges:
    h = deepcopy(g)
    h[u] -= {v}
    h[v] -= {u}
    if not is_connected(h, n):
        ans += 1
print(ans)
