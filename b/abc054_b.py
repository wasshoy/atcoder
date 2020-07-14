
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


n, m = LI()
a = SR(n)
b = SR(m)
ans = 'No'
for h in range(n - m + 1):
    for w in range(n - m + 1):
        is_ok = True
        for i in range(m):
            for j in range(m):
                if a[h + i][w + j] != b[i][j]:
                    is_ok = False
                    break
        if is_ok:
            ans = 'Yes'
            break
print(ans)
