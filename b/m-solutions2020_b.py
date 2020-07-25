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


a, b, c = LI()
k = I()
i = 0
while i < k:
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
    if a < b and b < c:
        break
    i += 1
    # print(a, b, c)
if a < b and b < c:
    print('Yes')
else:
    print('No')
