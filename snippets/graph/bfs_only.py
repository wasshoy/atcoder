# bfs のアルゴリズムの部分だけを記述
from collections import deque


INF = float('inf')


# g[i]: 頂点 i に隣接する頂点
def bfs(g, start):
    '''startからの最短距離のリストを返す（到達できないなら INF）'''
    n = len(g)
    d = [INF] * n
    que = deque([start])
    d[start] = 0
    while que:
        now = que.popleft()
        for nv in g[now]:
            if d[nv] != INF:
                continue
            que.append(nv)
            d[nv] = d[now] + 1
    return d
