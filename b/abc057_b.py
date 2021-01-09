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

# 6m AC
n, m = LI()
s = LIR(n)
c = LIR(m)
ans = []
for i in range(n):
    point = 0
    dist = 10**10
    for j in range(m):
        now_d = abs(s[i][0]-c[j][0]) + abs(s[i][1]-c[j][1])
        if now_d < dist:
            dist = now_d
            point = j
    ans.append(point+1)
print(*ans, sep='\n')
