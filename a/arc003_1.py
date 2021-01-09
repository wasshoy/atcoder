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

# 3m AC
n = I()
r = S()
s = 0
d = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
scores = [d[ri] for ri in r]
gpa = sum(scores) / n
print(gpa)
