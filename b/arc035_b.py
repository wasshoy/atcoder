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


# 20m弱? AC
INF = float('inf')
MOD = 10**9 + 7
n = I()
t = IR(n)
t.sort()
time = 0
penalty = 0
for ti in t:
    time += ti
    penalty += time
counter = Counter(t)
pat = 1
# 全体で高々 O(N)
# 種類が多いと個数が小さくなるし、個数が多いなら種類は少ない
# N = 10^4 のときでも、最大で 100種類がそれぞれ100個ずつあってもO(10^2 * 10 ^2)
cnt_1 = 0
cnt_2 = 0
for v in counter.values():
    for i in range(2, v+1):  # 階乗の計算
        pat *= i
        pat %= MOD
print(penalty)
print(pat)
