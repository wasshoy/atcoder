# 32m AC
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
s_c = list(s)
n = len(s)
ans = 0
i = 0
while i < n:
    if i < n - 1 and s[i] + s[i+1] == '25':
        i += 2
    else:
        s_c[i] = '.'
        i += 1
s_c = ''.join(s_c).split('.')
for elem in s_c:
    m = len(elem) // 2
    if m > 0:
        ans += m * (m + 1) // 2
print(ans)
