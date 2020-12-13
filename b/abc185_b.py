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

n, m, t = LI()
a = []
b = []
for _ in range(m):
    ai, bi = LI()
    a.append(ai)
    b.append(bi)

ans = 'Yes'
bat = n
time = 0
for i in range(m):
    bat -= a[i] - time
    if bat <= 0:
        print('No')
        exit()

    time = a[i]
    bat += b[i] - a[i]
    time = b[i]
    bat = min(bat, n)
# 帰宅
bat -= t - b[-1]
if bat <= 0:
    ans = 'No'
print(ans)
