import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


# 木 ： 閉路を持たない連結グラフ
# 閉路を持たない ： 全ての頂点に関して、自分からスタートして自分に戻ってこないようなグラフ
# 性質 : 辺数 + 1 = 頂点数 (Union-Find 木 で解く方法)


n, m = LI()
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = LI()
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)

visited = set()


def dfs(now, prev):  # どこから来たかを表す prev
    global is_tree
    visited.add(now)
    for v in edges[now]:
        if v == prev:  # 来た頂点以外に向かう
            continue
        if v in visited:  # 再び訪れてしまった場合
            is_tree = False
        else:
            visited.add(v)
            dfs(v, now)


ans = 0
# 各頂点から dfs を行う
for i in range(n):
    if i not in visited:  # 前回の dfs で探索されていない場合 (= 別の連結グラフの頂点)
        is_tree = True  # 今回探索する連結グラフが木かどうか
        dfs(i, -1)
        if is_tree:
            ans += 1
print(ans)
