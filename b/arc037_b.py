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
ans = 0
visited = set()


def dfs(now, prev):  # どこから来たかを表す prev
    global is_tree
    # print(f'{visited=}')
    # print(f'@ {now} (come from {prev}) ')
    visited.add(now)
    for v in edges[now]:
        # print(f'search {v}')
        if v != prev:  # 来た頂点以外に向かう
            if v in visited:  # 再び訪れてしまった場合
                # print(f'not tree.')
                is_tree = False
                # print(f'{is_tree=}')
            else:
                # print(f'go to {v}')
                visited.add(v)
                dfs(v, now)


# 各頂点から dfs を行う
for i in range(n):
    # print(f'{i=}, {ans=}')
    if i not in visited:  # 前回の dfs で探索されていない場合 (= 別の連結グラフの頂点)
        is_tree = True  # 今回探索する連結グラフが木かどうか
        dfs(i, -1)
        # print(f'(global){is_tree=}')
        if is_tree:
            # print(f'add ans 1')
            ans += 1
print(ans)
