import sys
from collections import deque
from itertools import product


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

h, w = LI()
s = [list(S()) for _ in range(h)]


def bfs(start):
    visited = [[False] * w for _ in range(h)]
    distances = [[-1] * w for __ in range(h)]
    start_h, start_w = start
    distances[start_h][start_w] = 0
    visited[start_h][start_w] = True
    queue = deque([[start_h, start_w]])
    while queue:
        now_h, now_w = queue.popleft()
        for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_h, next_w = now_h+dh, now_w+dw
            if not(0 <= next_h < h) or not(0 <= next_w < w) or s[next_h][next_w] == '#':
                continue
            if visited[next_h][next_w]:
                continue
            distances[next_h][next_w] = distances[now_h][now_w] + 1
            visited[next_h][next_w] = True
            queue.append([next_h, next_w])
    return distances


ans = 0
masu = [[i, j] for j in range(w) for i in range(h)]
for start in masu:
    start_h, start_w = start
    if s[start_h][start_w] == '#':
        continue
    d = bfs(start)
    max_d = 0
    for i in range(h):
        max_d = max(max_d, max(d[i]))
    ans = max(ans, max_d)
print(ans)
