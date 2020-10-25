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


n, q = LI()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = LI()
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)


counters = [0] * n
for _ in range(q):
    p, x = LI()
    p -= 1
    counters[p] += x  # いもす法の加算処理部分

# 深さ優先探索で根から子へ累積和を計算していく
queue = []
visited = [False] * n
queue.append(0)
visited[0] = True
while len(queue) > 0:
    parent = queue.pop()
    for child in graph[parent]:
        if not(visited[child]):
            visited[child] = True
            counters[child] += counters[parent]
            queue.append(child)

print(*counters)
