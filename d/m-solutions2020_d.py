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
ans = 1000
for i in range(n - 1):
    kabu = 0
    if a[i] < a[i+1]:
        # 出来るだけ買う
        kabu = ans // a[i]
    # 買った株があれば i + 1日目 に売る
    if kabu > 0:
        ans += (a[i + 1] - a[i]) * kabu
print(ans)
