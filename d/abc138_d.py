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

# いもす法 を木構造（根付き木）に適用
n, q = LI()
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = LI()
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

counters = [0] * n
for _ in range(q):
    p, x = LI()
    p -= 1
    counters[p] += x

# 親から子へ値を伝えていく
queue = [0]
visited = [False] * n
visited[0] = True
while queue:
    parent = queue.pop()
    for child in edges[parent]:
        if visited[child]:
            continue
        visited[child] = True
        counters[child] += counters[parent]
        queue.append(child)
print(*counters)
