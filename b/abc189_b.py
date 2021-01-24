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

n, x = LI()
al = 0
ans = 0
vp = LIR(n)
for i in range(n):
    v, p = vp[i][0], vp[i][1]
    al += v*p
    if al > 100*x:
        print(i+1)
        exit()

print(-1)
