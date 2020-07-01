# 11m AC
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
a = LI()
b = []
iodd = a[::2]
ieven = a[1::2]
if n % 2 == 0:
    b = ieven[::-1] + iodd
else:
    b = iodd[::-1] + ieven
print(*b)
