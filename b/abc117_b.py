import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
l = LI()
max_l = max(l)
max_i = l.index(max(l))
l.pop(max_i)
if max_l < sum(l):
    print('Yes')
else:
    print('No')
