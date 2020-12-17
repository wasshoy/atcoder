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
s = S()

left_b = 0
right_w = s.count('.')
ans = right_w
curr = s[0]

# 現在地より左にある黒とそれより右にある白の和を計算
for si in s:
    if si == '.':
        right_w -= 1
    else:
        left_b += 1
    ans = min(ans, left_b+right_w)
print(ans)
