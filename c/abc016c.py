from collections import deque
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]


INF = float('inf')


def bfs(g, start):
    '''startからの最短距離を返す'''
    n = len(g)
    d = [INF] * n
    que = deque([start])
    d[start] = 0
    while que:
        curr = que.popleft()
        for nxt in g[curr]:
            if d[nxt] != INF:
                continue
            que.append(nxt)
            d[nxt] = d[curr] + 1
    return d


def main():
    n, m = LI()
    ab = LIR(m)
    edges = [[] for _ in range(n)]
    for a, b in ab:
        a, b = a - 1, b - 1
        edges[a].append(b)
        edges[b].append(a)
    # 各ユーザーからの最短距離が 2 のユーザーの数を出力
    for i in range(n):
        d = bfs(edges, i)
        print(d.count(2))


main()
