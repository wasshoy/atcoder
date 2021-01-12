import sys


def input(): return sys.stdin.readline().strip()


# 5m AC
n, s, t = map(int, input().split())
w = int(input())
a = [int(input()) for _ in range(n-1)]
ans = 1 if s <= w <= t else 0
for ai in a:
    w += ai
    if s <= w <= t:
        ans += 1
print(ans)
