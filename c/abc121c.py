# https://atcoder.jp/contests/abc121/tasks/abc121_c
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ans = 0
drink_num = 0
# 値段に関してソート
ab.sort(key=lambda shop: shop[0])
for i in range(n):
    if (drink_num + ab[i][1]) > m:
        ans += ab[i][0] * (m - drink_num)
        drink_num += m - drink_num
        break
    ans += ab[i][0] * ab[i][1]
    drink_num += ab[i][1]
print(ans)