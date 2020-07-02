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
ans = 0
for i in range(2 ** (n - 1)):
    res = '' + s[0]
    for j in range(n - 1):
        if i >> j & 1:
            res += '+'
        res += s[j + 1]
    res = list(map(int, res.split('+')))
    ans += sum(res)
print(ans)
