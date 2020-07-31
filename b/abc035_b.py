# 15m AC + 2WA
from collections import Counter
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


s = S()
n = len(s)
t = I()
c = Counter(s)
x, y = 0, 0
ex_cnt = 0
for elem in s:
    if elem == 'L':
        x += -1
    elif elem == 'R':
        x += 1
    elif elem == 'U':
        y += 1
    elif elem == 'D':
        y -= 1
    else:
        ex_cnt += 1
# print(x, y, ex_cnt)
if t == 1:
    ans = abs(x) + abs(y) + ex_cnt
else:
    ans = abs(x) + abs(y) - ex_cnt
    if ans < 0:
        if abs(ans) % 2 == 0:
            ans = 0
        else:
            ans = 1
print(ans)
