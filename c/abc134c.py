# https://atcoder.jp/contests/abc134/tasks/abc134_c
n = int(input())
a = [int(input()) for _ in range(n)]
sort_a = sorted(a)
max_a = max(a)
max_ind = 0
for i in range(n):
    if a[i] == max_a: max_ind = i
for i in range(n):
    ans = max_a if i != max_ind else sort_a[-2]
    print(ans)