import sys
from collections import deque


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
c = SR(h)
start = [0, 0]
goal = [0, 0]
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            start = [i, j]
        if c[i][j] == 'g':
            goal = [i, j]

d = [[INF] * w for _ in range(h)]


def bfs_01(maze, start, costs):
    sh, sw = start
    costs[sh][sw] = 0
    deq = deque([[sh, sw]])
    while deq:
        curr_h, curr_w = deq.popleft()
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_h = curr_h + dh
            next_w = curr_w + dw
            if not(0 <= next_h < h) or not(0 <= next_w < w):
                continue
            if costs[next_h][next_w] != INF:
                continue
            if maze[next_h][next_w] == '#':  # 壁なら破壊コスト +1
                costs[next_h][next_w] = costs[curr_h][curr_w] + 1
                deq.append([next_h, next_w])  # 末尾に加える
            else:  # 道ならコスト据え置き
                costs[next_h][next_w] = costs[curr_h][curr_w]
                deq.appendleft([next_h, next_w])  # 先頭に加える
    return d


d = bfs_01(c, start, d)
gh, gw = goal
ans = 'YES' if d[gh][gw] <= 2 else 'NO'
print(ans)
