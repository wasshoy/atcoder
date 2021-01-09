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

# 4m AC
n = I()
a = LI()
a = [v-1 for v in a]
ans = 0
for i in range(n):
    if a[a[i]] == i:
        ans += 1
print(ans//2)
