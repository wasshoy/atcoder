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


n = I()
# 1 ,..., Xまでの和がN以上ならば、必ずちょうどNにできる
# Xまでの和がちょうどNでないとき、その差の数を1つ除けば答えになる
s = 0
ans = []
for i in range(1, n//2 + 2):
    s += i
    ans.append(i)
    if s >= n:
        break

diff = s - n
if diff > 0:
    ans.remove(diff)
print(*ans, sep='\n')
