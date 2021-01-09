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
MOD = 10**9 + 7


# not AC
n = I()
edges = []
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = LI()
    a -= 1
    b -= 1
    edges.append([a, b])
    graph[a].append(b)
    graph[b].append(a)


# 適当に頂点1を根とした根付き木と見る
depth = [-1] * n  # 深さは木の上下関係を考えるときに必要
# 深さを求める dfs
depth[0] = 0
que = [0]
while que:
    now = que.pop()
    for nxt in graph[now]:
        if depth[nxt] == -1:  # まだ深さが未定義
            depth[nxt] = depth[now] + 1
            que.append(nxt)

counters = [0] * n
q = I()
for _ in range(q):
    t, e, x = LI()
    e -= 1
    start = edges[e][0] if t == 1 else edges[e][1]
    not_pass = edges[e][1] if t == 1 else edges[e][0]

    if depth[start] < depth[not_pass]:  # 開始地点が通らない頂点より下
        # 通らない頂点の部分木以外に足すようにする
        counters[0] += x  # 根に足す
        counters[not_pass] -= x  # 通らない頂点の部分木は引く
    else:
        counters[start] += x  # 開始地点の部分木に足す

que = [0]
while que:
    now = que.pop()
    for nxt in graph[now]:
        if depth[now] < depth[nxt]:  # 現在地点の子に伝播
            counters[nxt] += counters[now]
            que.append(nxt)


print(*counters, sep='\n')
