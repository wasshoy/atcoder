import sys
import heapq


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


def dijkstra(start, g):
    # 頂点 start へ向かう最小コストを返す
    n = len(g)
    hq = [(0, start)]
    heapq.heapify(hq)
    costs = [float('inf')] * n  # start から各頂点へ向かう最小コスト
    costs[start] = 0
    while hq:
        c, v = heapq.heappop(hq)
        if c > costs[v]:
            continue

        for d, u in g[v]:
            temp_c = d + costs[v]
            if temp_c < costs[u]:
                costs[u] = temp_c
                heapq.heappush(hq, (temp_c, u))
    return costs


n, m = LI()
ans = float('inf')
# costs[i] : 頂点 i から向かえる頂点 j とそのコストのタプル
w_graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = LI()
    a, b = a-1, b-1
    w_graph[a].append((t, b))
    w_graph[b].append((t, a))

ans = float('inf')
for i in range(n):
    worst = max(dijkstra(i, w_graph))
    ans = min(ans, worst)
print(ans)
