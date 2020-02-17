# https://atcoder.jp/contests/abc115/tasks/abc115_c
n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]
h.sort()
diff = h[k-1] - h[0]
for i in range(1, n-k+1):
    diff = min(diff, h[i+k-1] - h[i])
print(diff)