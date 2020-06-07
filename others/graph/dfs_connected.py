# 無向グラフの連結成分の個数を数える
import sys
sys.setrecursionlimit(10 ** 7)


n, m = map(int, input().split())
is_seen = [False for _ in range(n)]
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


def dfs(graph, v):
    is_seen[v] = True
    for next_v in graph[v]:
        if is_seen[v]:
            continue
        dfs(graph, next_v)


def main():
    count = 0
    for v in range(n):
        if is_seen[v]:
            continue
        dfs(g, v)
        count += 1
    print(count)
