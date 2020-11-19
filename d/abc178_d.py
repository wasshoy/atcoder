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
MOD = 10**9 + 7
s = I()
# 7 = 3 + 4 = 4 + 3 3通り
# 9 = 3 + 3 + 3 = 3 + 6 = 4 + 5 = 5 + 4 = 6 + 3 = 9 ６通り
# 項の条件が 1以上のとき S個のボールの S-1個の間に 0 ~ S-1個の仕切りを入れる場合の数 = 2^(S-1) 通り （仕切りをいれるか・いれないかの ２つ)
# dp[i] *= 最後に仕切った場所が i であるようなときの個数 ただし、両端も仕切る場所に考える (dp[0] = 1 (S = S))
# 例 : dp[6] = dp[6 - 3] + dp[3]
dp = [0] * (s+1)
dp[0] = 1  # {S}
for i in range(1, s+1):
    for j in range(0, (i-3)+1):
        dp[i] += dp[j]
        dp[i] %= MOD
print(dp[s])
