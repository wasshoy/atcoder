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

# 25
n = I()
a = LI()
cumsum = [0]
sumi = 0
for ai in a:
    sumi += ai
    cumsum.append(sumi)

cumsum_max = [0]
for ci in cumsum[1:]:
    cumsum_max.append(max(ci, cumsum_max[-1]))

ans = 0
curr = 0
for i in range(1, n+1):
    ans = max(ans, curr+cumsum_max[i])
    curr += cumsum[i]
print(ans)
