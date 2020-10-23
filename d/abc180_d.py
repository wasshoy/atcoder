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

# 1WA 35m AC
x, y, a, b = LI()
exp = 0
while True:
    if a*x < b+x and a*x < y:
        x = a*x
        exp += 1
    else:
        break

exp += (y-x-1) // b
print(exp)
