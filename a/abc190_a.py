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


INF = float('inf')
MOD = 10**9 + 7

a, b, c = LI()
if a == b:
    if c == 1:
        print('Takahashi')
    else:
        print('Aoki')
elif a > b:
    print('Takahashi')
else:
    print('Aoki')
