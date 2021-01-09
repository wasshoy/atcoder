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

# 1WA + 4m AC
s = S()
n = len(s)
is_ok = False
for i in range(n):
    for j in range(i, n):
        if s[:i] + s[j:] == 'keyence':
            print('YES')
            exit()
print('NO')
