import heapq
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n, m = LI()
a = LI()
a = list(map(lambda x: -1 * x, a))
heapq.heapify(a)
for _ in range(m):
    price = -1 * heapq.heappop(a)  # 現時点での最大値をO(log N)で取得
    heapq.heappush(a,  -1 * (price // 2))
print(-1 * sum(a))
