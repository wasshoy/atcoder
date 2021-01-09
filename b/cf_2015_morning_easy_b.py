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

# 5m AC
n = I()
s = S()
if n % 2 != 0:
    print(-1)
    exit()
s1 = s[:n//2]
s2 = s[n//2:]
ans = 0
for i in range(n//2):
    if s1[i] != s2[i]:
        ans += 1
print(ans)
