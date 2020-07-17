# 22m AC 1WA
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
t = IR(n)
ans = INF
if n == 1:
    ans = t[0]
elif n == 2:
    ans = max(t)
elif n == 3:
    ans = min(
        [max(t[0] + t[1], t[2]),
         max(t[0] + t[2], t[1]),
         max(t[1] + t[2], t[0])]
    )
else:
    ans = min(
        ans,
        max(t[0], sum(t[1:])),
        max(t[1], t[0] + t[2] + t[3]),
        max(t[2], t[0] + t[1] + t[3]),
        max(t[3], sum(t[:3]))
    )
    ans = min(
        [
            ans,
            max(t[0] + t[1], t[2] + t[3]),
            max(t[0] + t[2], t[1] + t[3]),
            max(t[0] + t[3], t[2] + t[1]),
        ]
    )
print(ans)
