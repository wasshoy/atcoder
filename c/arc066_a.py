import sys
from collections import Counter


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# (MOD の書き間違いにより）3WA + 37m AC
n = I()
a = LI()
MOD = 10**9 + 7
c = Counter(a)

# 矛盾が間違っていないか確認
for k, v in c.items():
    if k == 0:
        if n % 2 != 0:
            if v != 1:
                print(0)
                exit()
        else:
            if v != 0:
                print(0)
                exit()

    if v > 2 or (n+k) % 2 == 0:  # 偶奇が一致
        print(0)
        exit()

ans = 1
for _ in range(n//2):
    ans *= 2
    ans %= MOD
print(ans)
