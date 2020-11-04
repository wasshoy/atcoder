# ワーシャルフロイド法: グラフの各頂点からの最短距離を求めるアルゴリズム
# 適している問題： あらゆるグラフの最短経路問題
# 計算量: O(N^3)
# 参考 https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%85%A8%E7%82%B9%E5%AF%BE%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%95%EF%BC%88%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95


import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


# c[i][j] : 頂点 i から j へ向かう最小コストを返す
def warshall_floyd(c):
    n = len(c)  # 頂点数
    for k in range(n):  # 中継点
        for i in range(n):  # 始点
            for j in range(n):  # 終点
                # 現時点の i から j へ向かうコスト と k を経由して j に向かうコスト の小さい方
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    return c
