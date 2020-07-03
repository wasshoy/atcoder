# 24m AC 解法からサンプル通るまでがかなりかかってしまった
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
a = [0] + a + [0]
sum_a = sum([abs(a[i] - a[i - 1]) for i in range(1, n + 2)])
ans = []
for i in range(1, n + 1):
    diff = - abs(a[i] - a[i - 1]) - abs(a[i + 1] - a[i]) + \
        abs(a[i + 1] - a[i - 1])
    cost = sum_a + diff
    ans.append(cost)
print(*ans, sep='\n')
