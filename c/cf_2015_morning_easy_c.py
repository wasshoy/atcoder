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

# 25m + 2RE AC
n, k, m, r = LI()
s = IR(n-1)

s.sort(reverse=True)
if k >= n:
    ans = max(0, k*r - sum(s))
    if ans > m:
        print(-1)
    else:
        print(ans)
    exit()

# k < n
sum_s = sum(s[:k])
if sum_s >= k*r:
    print(0)
else:
    min_s = s[:k][-1]
    ans = k*r - sum_s + min_s
    if ans > m:
        print(-1)
    else:
        print(ans)
