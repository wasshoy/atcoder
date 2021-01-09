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
s = S()
t = S()
ans = 0
res = s[:]
if s == t:
    print(0)
    exit()
for _ in range(len(s)):
    res = res[-1] + res[:-1]
    ans += 1
    if res == t:
        print(ans)
        exit()
print(-1)
