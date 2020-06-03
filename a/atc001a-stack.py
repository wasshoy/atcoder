from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
si, sj = 0, 0
gi, gj = 0, 0
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            si = i
            sj = j
        if c[i][j] == 'g':
            gi = i
            gj = j

is_seen = [[False for j in range(w)] for i in range(h)]
stack = deque([[si, sj]])
while stack:
    now_i, now_j = stack.pop()
    is_seen[now_i][now_j] = True
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_i = now_i + i
        next_j = now_j + j
        # 迷路の外もしくは壁
        if not(0 <= next_i <= h - 1) or not(0 <= next_j <= w - 1) or c[next_i][next_j] == '#':
            continue
        if is_seen[next_i][next_j] == False:
            stack.append([next_i, next_j])
    if is_seen[gi][gj]:
        print('Yes')
        sys.exit()

print('No')
