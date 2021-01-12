import sys


def input(): return sys.stdin.readline().strip()


INF = float('inf')
MOD = 10**9 + 7

# not AC
n = int(input())
a = list(map(int, input().split()))
a = a
s = sum(a)
# 山1の雨量を求める
odd_s = sum([v for i, v in enumerate(a[1:], start=1) if i % 2 != 0])
ans = [s - 2*odd_s]
print(ans)
# どちらか隣の山の雨量が決定すると自身も決定するので、順番に求めていく
for i in range(1, n):
    ans.append(2*a[i-1] - ans[i-1])
print(*ans)
