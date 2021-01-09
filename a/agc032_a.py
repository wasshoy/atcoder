import sys
from collections import deque


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 59m AC
n = I()
b = LI()
is_ok = True
res = []
while len(b) != 0:
    pop_i = -1
    pop_v = -1
    for i, v in list(enumerate(b))[::-1]:
        if b[i] == i+1:
            pop_i = i
            pop_v = v
            break
    if pop_i == -1:
        is_ok = False
        break
    else:
        res.append(b.pop(pop_i))

if is_ok:
    print(*res[::-1], sep='\n')
else:
    print(-1)
