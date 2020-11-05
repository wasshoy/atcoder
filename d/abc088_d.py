from collections import deque
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
# (h, w) が  (i, j) に対応
h, w = LI()
maze = [list(S()) for _ in range(h)]
dists = [[-1] * w for _ in range(h)]
direction_d = {'right': (0, 1), 'down': (1, 0),
               'left': (0, -1), 'up': (-1, 0)}
white_cnt = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dists[i][j] = INF
            white_cnt += 1
dists[0][0] = 0
que = deque([[0, 0]])
while que:
    y, x = que.popleft()
    for direction in ['right', 'down', 'left', 'up']:
        i, j = direction_d[direction]
        next_y = y + i
        next_x = x + j
        if not(0 <= next_y < h) or not(0 <= next_x < w):
            continue
        if maze[next_y][next_x] == '#':
            continue
        if dists[y][x]+1 < dists[next_y][next_x]:
            dists[next_y][next_x] = dists[y][x] + 1
            que.append([next_y, next_x])
if dists[h-1][w-1] in {-1, INF}:
    print(-1)
else:
    ans = white_cnt - (dists[h-1][w-1]+1)
    print(ans)
