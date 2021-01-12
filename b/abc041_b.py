import sys


def input(): return sys.stdin.readline().strip()


MOD = 10**9 + 7

# 2m AC
a, b, c = map(int, input().split())
ans = a * b
ans %= MOD
ans *= c
ans %= MOD
print(ans)
