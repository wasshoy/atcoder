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
k = 0
pre_w = ''
i = 0
while i < n:
    now_w = s[i]
    if now_w == pre_w:
        i += 1
        if i > n-1:
            break
        now_w += s[i]
    k += 1
    pre_w = now_w
    i += 1
print(k)
