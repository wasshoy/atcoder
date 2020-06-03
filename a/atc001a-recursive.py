# 再帰関数でdfs
from collections import deque
import sys

sys.setrecursionlimit(10**7)


def input(): return sys.stdin.readline().rstrip()


h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
gi, gj = 0, 0
si, sj = 0, 0
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            si = i
            sj = j
        if c[i][j] == 'g':
            gi = i
            gj = j


is_seen = [[False for j in range(w)] for i in range(h)]


def dfs(x, y):
    # 範囲外、訪問済み、もしくは壁なら何もしない
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == '#':
        return
    if is_seen[x][y]:
        return
    if c[x][y] == 'g':
        print('Yes')
        sys.exit()

    is_seen[x][y] = True
    # 上下左右を更に探索
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)


dfs(si, sj)

print('No')
