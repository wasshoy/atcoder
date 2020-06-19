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
a = [(i, v) for i, v in enumerate(a)]
a = sorted(a, key=lambda x: x[1], reverse=True)
a = [i + 1 for i, v in a]
print(*a, sep='\n')
