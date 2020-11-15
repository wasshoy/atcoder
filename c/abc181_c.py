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


def d(a, b):
    ax, ay = a
    bx, by = b
    return math.sqrt((ax - bx)**2 + (ay - by)**2)


n = I()
xy = []
for _ in range(n):
    x, y = LI()
    xy.append((x, y))

for i in range(n):
    for j in range(i):
        for k in range(j):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            # (x3, y3) が(0, 0) になるように全体をずらす
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            # 傾きを比較
            if x2 * y1 == x1 * y2:
                print('Yes')
                exit()
print('No')
