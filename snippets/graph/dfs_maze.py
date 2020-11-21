h = 4
w = 3


def dfs(maze: list, start, visited: list):
    '''
    迷路形式で入力が与えられた場合の dfs
    maze: maze[i][j]: i 列 j 行のマス
    start: start = (start_y, start_x) 開始マス
    visted: visted[i][j]: i 列 j 行のマスに訪れたかどうか
    '''
    start_y, start_x = start
    visited[start_y][start_x] = True
    for i, j in ((0, 1), (1, 0)):
        next_y = start_y + i
        next_x = start_x + j
        if not(0 <= next_y < h) or not(0 <= next_x < w):
            continue
        if maze[next_y][next_x] == '#':
            continue
        if not(visited[next_y][next_x]):
            dfs(maze, (next_y, next_x), visited)
    return visited
