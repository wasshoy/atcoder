# 29
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


def calc_cumsum(l):
    cumsum = [0]
    for i in l:
        cumsum.append(cumsum[-1] + i)
    return cumsum


n = I()
a = LI()
if sum(a) % n != 0:
    print(-1)
    exit()
avg = sum(a) // n
ans = 0
cumsum = calc_cumsum(a)
# 各橋を隔てて左と右の人数の合計が各島に必要な人数になっていなければ橋をかける
for i in range(n - 1):
    if cumsum[i+1] != avg * (i+1) or cumsum[n] - cumsum[i+1] != avg * (n-1-i):
        ans += 1
print(ans)
