
import sys


sys.setrecursionlimit(10**7)


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n, m = LI()
a = LI()
b = LI()
if n < m:
    print('NO')
    sys.exit()

a.sort(reverse=True)
b.sort(reverse=True)
for ai, bi in zip(a, b):
    if ai >= bi:
        continue
    else:
        print('NO')
        sys.exit()
print('YES')
