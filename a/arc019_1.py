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
d = {'O': 0, 'D': 0, 'I': 1, 'Z': 2, 'S': 5, 'B': 8}
ans = ''
for si in s:
    if si in d.keys():
        ans += str(d[si])
    else:
        ans += si
print(ans)
