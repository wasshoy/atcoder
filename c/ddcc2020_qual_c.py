import sys
def input(): return sys.stdin.readline().strip()


# 非自力AC
h, w, k = map(int, input().split())
s = [input() for _ in range(h)]
ans = [[-1] * w for _ in range(h)]
strb_n = 1

# イチゴがある部分を確定させる
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = strb_n
            strb_n += 1

# 四方から確定していない部分を埋めていく
# 上がイチゴならそのイチゴの一部とする
for i in range(1, h):
    for j in range(w):
        if ans[i][j] == -1 and ans[i-1][j] != -1:
            ans[i][j] = ans[i-1][j]
# 下がイチゴならそのイチゴの一部とする
for i in reversed(range(h-1)):
    for j in range(w):
        if ans[i][j] == -1 and ans[i+1][j] != -1:
            ans[i][j] = ans[i+1][j]
# 左がイチゴならそのイチゴの一部とする
for i in range(h):
    for j in range(1, w):
        if ans[i][j] == -1 and ans[i][j-1] != -1:
            ans[i][j] = ans[i][j-1]
# 右がイチゴならそのイチゴの一部とする
for i in range(h):
    for j in reversed(range(w-1)):
        if ans[i][j] == -1 and ans[i][j+1] != -1:
            ans[i][j] = ans[i][j+1]
for i in range(h):
    print(*ans[i])
