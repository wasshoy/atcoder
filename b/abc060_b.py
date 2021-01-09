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

# 24m AC
a, b, c = LI()
for k in range(a+1):
    for t in range(1, b+1):
        if t*a == k*b + c:
            print('YES')
            exit()
print('NO')
