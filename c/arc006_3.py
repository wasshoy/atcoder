import sys
import bisect


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 45m? AC
n = I()
w = IR(n)
tops = []  # 各山の一番上
for wi in w:
    if len(tops) < 1:
        tops.append(wi)
    else:
        i = bisect.bisect_left(tops, wi)
        if i == len(tops):
            # どこの山の上にも置けない場合
            tops.append(wi)
        else:
            tops[i] = wi
ans = len(set(tops))
print(ans)
