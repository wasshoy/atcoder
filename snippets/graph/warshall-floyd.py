# ワーシャルフロイド法: グラフの各頂点からの最短距離を求めるアルゴリズム
# 適している問題： あらゆるグラフの最短経路問題
# 計算量: O(N^3)
# 参考 https://juppy.hatenablog.com/entry/2018/11/01/%E8%9F%BB%E6%9C%AC_python_%E5%85%A8%E7%82%B9%E5%AF%BE%E6%9C%80%E7%9F%AD%E7%B5%8C%E8%B7%AF%E6%B3%95%EF%BC%88%E3%83%AF%E3%83%BC%E3%82%B7%E3%83%A3%E3%83%AB%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E6%B3%95


import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


def warsharll_floyd(d):
    n = len(d)
    # ワーシャルフロイド法のアルゴリズム部分
    for k in range(n):  # iからjへ向かう途中に中継する頂点
        for i in range(n):  # 始点
            for j in range(n):  # 終点
                # 現時点のiからjへ向かうコスト と kを経由してjに向かうコストの小さい方
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


# abc012dの解法
def main():
    n, m = LI()
    # graph[i][j]: 頂点iとjをつなぐ辺の重み(存在しない場合はinf)
    graph = [[float("inf") if i != j else 0 for j in range(n)]
             for i in range(n)]
    for _ in range(m):
        a, b, t = LI()
        a, b = a - 1, b - 1
        # 無向グラフ
        graph[a][b] = t
        graph[b][a] = t

    d = warsharll_floyd(graph)
    # print(*d, sep='\n')
    ans = float('inf')
    for i in range(n):
        ans = min(ans, max(d[i]))
    print(ans)


main()
