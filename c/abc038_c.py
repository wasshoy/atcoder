import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def ST(): return input()
def LST(): return input().split()


INF = float('inf')

N = I()
a = LI()
ans = 0
curr = a[0]
r = 1
for l in range(N):
    # l に対して条件を満たす最大の r を求める
    while r < N and (r == l or a[r-1] < a[r]):  # r = l のときも要素は 1つだが条件を満たす
        r += 1
    ans += r - l
print(ans)
