import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


x, n = LI()
p = LI()
if n == 0:
    print(x)
    sys.exit()

ans = 10000
for i in range(-1, 102):
    if abs(x - i) < abs(x - ans) and i not in p:
        ans = i
print(ans)
