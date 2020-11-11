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

# 76m AC
n, k = LI()
ans = 0
k = abs(k)
for x in range(2+k, 2*n+1):
    y = x - k
    if x % 2 == 0:
        cnt_x = (x//2 - max(0, x-1-n) - 1) * 2 + 1
    else:
        cnt_x = (x//2 - max(0, x-1-n)) * 2
    if y % 2 == 0:
        cnt_y = (y//2 - max(0, y-1-n) - 1) * 2 + 1
    else:
        cnt_y = (y//2 - max(0, y-1-n)) * 2
    ans += cnt_x * cnt_y
print(ans)
