# dfsのみを行うもろもろ
from collections import defaultdict
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


INF = float('inf')
sys.setrecursionlimit(10 ** 7)


def dfs(g, start, visited):
    ''' startから訪問できる頂点の集合を返す'''
    visited.add(start)
    for v in g[start]:
        if v not in visited:
            dfs(g, v, visited)
    return visited


def is_connected(g, node_cnt):
    '''連結グラフかどうか'''
    visited = dfs(g, 1, set())
    if len(visited) == node_cnt:
        return True
    else:
        return False


def main():
    n, m = LI()
    edges = [LI() for _ in range(m)]
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)
