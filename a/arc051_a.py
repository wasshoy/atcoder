import sys
import math


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 54
x1, y1, r = LI()
x2, y2, x3, y3 = LI()
yes_no = ['NO', 'YES']
have_red = True
have_blue = True
# 円が長方形に内包されているか
if x2 <= x1-r and x1+r <= x3 and y2 <= y1-r and y1+r <= y3:
    have_red = False

# 長方形が円に内包されているか
else:
    ds = [
        (x1-x2)**2 + (y1-y2)**2,
        (x3-x1)**2 + (y1-y2)**2,
        (x3-x1)**2 + (y3-y1)**2,
        (x1-x2)**2 + (y3-y1)**2
    ]
    if any(True if d > r**2 else False for d in ds):
        have_blue = True
    else:
        have_blue = False


print(yes_no[have_red])
print(yes_no[have_blue])
