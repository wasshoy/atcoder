# 57
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
ngs = [I() for _ in range(3)]
if n in ngs:
    print('NO')
    exit()
ngs = [i for i in ngs if i < n]
ngs.sort()
if len(ngs) < 1:
    print('YES')
    exit()
if len(ngs) == 3 and ngs[2]-ngs[1] == 1 and ngs[1]-ngs[0] == 1:
    print('NO')
    exit()

# 貪欲法的な解法
ngs = set(ngs)
for _ in range(100):
    if n-3 not in ngs:
        n -= 3
    else:
        if n-2 not in ngs:
            n -= 2
        else:
            n -= 1
if n <= 0:
    print('YES')
else:
    print('NO')
