# https://atcoder.jp/contests/abc007/tasks/abc007_3
import sys
from collections import deque


def main():
    r, c = map(int, sys.stdin.readline().split())
    sy, sx = map(int, sys.stdin.readline().split())
    gy, gx = map(int, sys.stdin.readline().split())
    maze = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if maze[i][j] == '.':
                maze[i][j] = float('inf')
    # スタート地点の初期値
    maze[sy-1][sx-1] = 0
    # キュー（初期値はスタート地点）
    que = deque([[sy-1, sx-1]])
    # queが空になる=全部のマスの値を埋めるまで
    while(que):
        # print(que)
        y, x = que.popleft()
        # (y, x)の隣接する4マスを見る
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            next_y = y + i
            next_x = x + j
            # 壁ならスキップ
            if maze[next_y][next_x] == '#':
                continue
            if maze[y][x] + 1 < maze[next_y][next_x]:
                maze[next_y][next_x] = maze[y][x] + 1
                #print(f'maze[{next_y}][{next_x}] = {maze[next_y][next_x]}')
                que.append([next_y, next_x])
    print(maze[gy-1][gx-1])


main()
