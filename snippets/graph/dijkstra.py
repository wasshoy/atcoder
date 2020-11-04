# ダイクストラ法： 重み付きグラフの最短経路問題を解くアルゴリズム(経路と距離が求められる)
# 最小コストで行けるところをひたすら更新していく
# 適している問題： 重みあり（非負）グラフの最短経路問題
# 計算量: O(N^2)
# 優先度付きキューを使った場合: O((N + 辺数) * log N) とかになる

# pythonでの実装： 最小コストで行ける頂点を探す動作を
# 優先度付きキューをheapqモジュールで実現 (参考： https://nashidos.hatenablog.com/entry/2019/12/28/192207)
# 優先度付きキュー： 最大/最小値の探索が O(log 1) (リストだとO(N))
# 要素の追加/削除が O(log N)
# listのheap化: O(N)


import heapq
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


def dijkstra(start, g):
    # start から 各頂点へ向かう最小コストを返す
    hq = [(0, start)]  # (かかるコスト, 頂点)
    heapq.heapify(hq)
    costs = [float('inf')] * len(g)  # 各頂点の最小コスト
    costs[start] = 0  # 開始地点は 0
    while hq:
        c, v = heapq.heappop(hq)
        # vへ向かうコストが現在のコストよりも大きければ（＝すでにコストが確定した頂点）更新しない
        if c > costs[v]:
            continue

        for d, u in g[v]:
            # v から u に向かうコストと現時点でのコストを比較
            if costs[v]+d < costs[u]:
                costs[u] = costs[v]+d
                heapq.heappush(hq, (costs[v]+d, u))
    return costs


# abc012の解法
def main():
    n, m = LI()
    graph = [[] for _ in range(n)]  # 各頂点に繋がる(頂点, 辺の重み)のリスト
    for _ in range(m):
        a, b, t = LI()
        a, b = a - 1, b - 1
        # 無向グラフ
        graph[a].append((t, b))
        graph[b].append((t, a))

    ans = float('inf')
    # 各頂点からその他の頂点に向かうのにかかる時間を計算
    for i in range(n):
        dist = dijkstra(i, graph)
        print(dist)
        ans = min(ans, max(dist))
    print(ans)


main()
