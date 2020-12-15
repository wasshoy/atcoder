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

n = I()
robots = []
# [腕の左端, 腕の右端] のリストにする
for _ in range(n):
    xi, li = LI()
    robots.append([xi-li, xi+li])
robots = sorted(robots, key=lambda x: x[1])  # 腕の右端の位置でソート
# 区間スケジューリング問題として解く
curr_x = -10**9 - 10
ans = 0
for xs, xt in robots:
    if curr_x <= xs:
        ans += 1
        curr_x = xt
print(ans)
