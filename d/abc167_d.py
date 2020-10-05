import sys
from collections import defaultdict


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


N, K = LI()
A = LI()
A = [v-1 for v in A]
if K <= N:
    now = 0
    for _ in range(K):
        now = A[now]
    print(now + 1)
    exit()

# 周期の開始地点を調べる
now = 0
t = 0  # 経過時間
first_visited_t_d = defaultdict(int)  # 初訪の時間
first_visited_t_d[now] = 0
start_period = 0  # 周期が開始する地点
start_period_t = 0  # 周期が開始する時間
period = 0  # 周期

while True:
    t += 1
    if A[now] in first_visited_t_d.keys():  # 再び訪れた場所が周期の開始地点
        start_period = A[now]
        start_period_t = first_visited_t_d[A[now]]
        period = t - first_visited_t_d[A[now]]
        break

    now = A[now]
    first_visited_t_d[now] = t

K -= start_period_t
K %= period
now = start_period
for _ in range(K):
    now = A[now]
print(now + 1)
