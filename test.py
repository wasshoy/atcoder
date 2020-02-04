# atcoderのテスト用
# ./iunput/input.txt に入力を書き込む
with open('./input/input.txt') as f:
    n, W = map(int, f.readline().split())
    wv = [list(map(int, f.readline().split())) for _ in range(n)]
w = [wv[i][0] for i in range(n)]
v = [wv[i][1] for i in range(n)]
inf = float('inf')
V = max(v)
vmax = 10**5+1
# dp[i][sum_v] 
# := i-1番目までの品物で価値がsum_vを超えないように選んだときの重さの総和の最小値
# 価値の合計はどれくらい大きくなるかわからないので十分に用意しとく
dp = [[inf for _ in range(vmax)] for _ in range(n+1)]
# 初期条件
dp[0][0] = 0
for i in range(n):
    for sum_v in range(vmax):
        # i番目の品物を選べるとき
        if sum_v - v[i] >= 0:
            dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v - v[i]] + w[i])
        # i番目の品物を選ばないとき
        dp[i+1][sum_v] = min(dp[i+1][sum_v], dp[i][sum_v])


# 最適解を探す
ans = 0
for sum_v in range(vmax):
    if dp[n][sum_v] <= W:
        ans = sum_v
print(ans)