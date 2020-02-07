# https://atcoder.jp/contests/abc132/tasks/abc132_c
n = int(input())
d = list(map(int, input().split()))
sort_d = sorted(d)
print(sort_d[n//2] - sort_d[n//2 - 1])