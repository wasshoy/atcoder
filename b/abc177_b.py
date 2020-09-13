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


s = S()
t = S()
if s == t:
    print(0)
    exit()

ans = len(t)
for i in range(len(s)-len(t)+1):
    # print(f'{i=}')
    now = 0
    for j in range(len(t)):
        # print(f'{(s[i+j], t[j])=}')
        if s[i+j] != t[j]:
            now += 1
    # print(f'{now=}')
    ans = min(ans, now)

print(ans)
