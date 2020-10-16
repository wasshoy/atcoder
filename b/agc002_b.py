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

# 20m AC
n, m = LI()
is_included_red = [False] * n
counts = [1] * n
is_included_red[0] = True
is_choiced = False
for _ in range(m):
    x, y = LI()
    x, y = x - 1, y - 1
    if counts[x] > 0:
        counts[x] -= 1
        counts[y] += 1
        if is_included_red[x]:
            is_included_red[y] = True
    if counts[x] == 0:
        is_included_red[x] = False


ans = 0
for elem in is_included_red:
    if elem:
        ans += 1
print(ans)
