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


INF = float('inf')


n = I()
a = LI()
a = list(map(lambda x: -x, a))
a = sorted(a)
l = []
heapq.heapify(l)
ans = 0
heapq.heappush(l, a[0])
for elem in a[1:]:
    ans += -heapq.heappop(l)
    heapq.heappush(l, elem)
    heapq.heappush(l, elem)
print(ans)
