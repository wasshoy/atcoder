# :20
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


x, y, a, b, c = LI()
p = sorted(LI())[::-1][:x]
q = sorted(LI())[::-1][:y]
r = sorted(LI())[::-1][:x+y]
bucket = []
bucket += [i for i in p]
bucket += [i for i in q]
bucket += [i for i in r]
bucket = sorted(bucket)[::-1]
ans = sum(bucket[:x+y])
print(ans)
