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
n = len(s)
a = [0] * (n + 1)
for i in range(len(s)):
    if '<' == s[i]:
        a[i + 1] = a[i] + 1
for i in reversed(range(len(s))):
    if '>' == s[i]:
        a[i] = max(a[i], a[i + 1] + 1)
print(sum(a))
