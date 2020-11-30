import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 25
N, K = LI()
ans = 0
# amari[x] : N以下の自然数で Kで割ったあまりが xである数の個数 = N以下の xの倍数の個数
amari = [0 for _ in range(K)]
for i in range(1, N+1):
    amari[i % K] += 1

for a in range(K):
    # 余りの和が Kの倍数なら条件を満たすので、余りだけ見れば良い
    b = (K-a) % K
    c = (K-a) % K
    if (b+c) % K != 0:
        continue
    ans += amari[a] * amari[b] * amari[c]  # a を 2a に変えても役割は変わらない
print(ans)
