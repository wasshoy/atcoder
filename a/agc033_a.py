import sys
from collections import deque
from functools import reduce


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 多点スタートの最短経路問題
# 通常のbfsでは開始地点は 1 つ
# 多点bfsでは開始地点を一気にぶっこむ


def bfs_multi_start(maze, starts, d):
    que = deque([])
    for start_y, start_x in starts:
        d[start_y][start_x] = 0
        que.append([start_y, start_x])
    while que:
        y, x = que.popleft()
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_y = y + i
            next_x = x + j
            if not(0 <= next_y < h) or not(0 <= next_x < w):
                continue
            if maze[next_y][next_x] == '#' or d[next_y][next_x] != -1:
                continue
            d[next_y][next_x] = d[y][x] + 1
            que.append([next_y, next_x])
    return d


h, w = LI()
a = [list(S()) for i in range(h)]
starts = []  # 多点スタートの位置
for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            starts.append((i, j))

d = [[-1] * w for _ in range(h)]
d = bfs_multi_start(a, starts, d)
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, d[i][j])
print(ans)
