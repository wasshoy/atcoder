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
MOD = 10**9 + 7

n = I()
ans = 0
x = []
y = []
for _ in range(n):
    xi, yi = LI()
    x.append(xi)
    y.append(yi)

for i in range(n):
    for j in range(i+1, n):
        katamuki = (y[i] - y[j]) / (x[i] - x[j])
        if -1 <= katamuki <= 1:
            ans += 1
print(ans)
