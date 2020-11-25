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


# 33
def cumsum(l):
    i = 0
    res = [0]
    for v in l:
        i += v
        res.append(i)
    return res


n, k = LI()
a = LI()
# 区間 [2, 5) の和 = cumsum_a[5] - cumsum_a[2]
cumsum_a = cumsum(a)

ans = 0
for i in range(n-k+1):
    ans += cumsum_a[i+k] - cumsum_a[i]
print(ans)
