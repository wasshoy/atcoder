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
# 7m AC
s = list(S())
n = I()
for _ in range(n):
    l, r = LI()
    l -= 1
    r -= 1
    s[l:r+1] = s[l:r+1][::-1]
print(''.join(s))
