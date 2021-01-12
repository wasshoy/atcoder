from itertools import product
h, w = map(int, input().split())
s = [input() for _ in range(h)]
ans = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        for dh, dw in product((-1, 0, 1), repeat=2):
            nh = i + dh
            nw = j + dw
            if s[i][j] != '#':
                continue
            ans[i][j] = '#'
            if 0 <= nh < h and 0 <= nw < w and s[nh][nw] == '.':
                ans[nh][nw] += 1
for i in range(h):
    print(''.join(map(str, ans[i])))
