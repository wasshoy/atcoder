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


x = I()

# 金額の範囲を考える
# どれか 1 個買うときの取りうる値段は 100, 101, ..., 105
# 2 個買うときは 200, 201, 202, 203, ..., 209, 210
# 3 個買うときは 300, 301, 302, ..., 315
# 1000 個買うときは 100000, 10001, ..., 105000 : 1001個以上は x の上限を超えるので考えなくて良い
# 各個数で取りうる金額の範囲内に x が入っているかどうかを確かめる
exists = False
for i in range(1, 1001):
    if 100*i <= x <= 105*i:
        exists = True
        break
print(1 if exists else 0)
