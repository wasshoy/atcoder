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

# 累積和を計算


def calc_cumsum(l):
    cumsum = [0]
    for i in l:
        cumsum.append(cumsum[-1] + i)
    return cumsum


n = I()
a = LI()
a.sort()
cumsum = calc_cumsum(a)
ans = 0
for i in range(n-1):
    ans += (cumsum[n] - cumsum[i+1]) - (n-(i+1))*a[i]
print(ans)
