# 20m? AC
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


def tribonacci(m, dp):
    for i in range(3, m):
        dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD
    return dp[m - 1]


n = I()
MOD = 10007
table = [None] * (10 ** 6 + 1)
table[0] = 0
table[1] = 0
table[2] = 1
ans = tribonacci(n, table)
print(ans)
