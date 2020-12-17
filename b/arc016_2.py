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

# 02
n = I()
x = SR(n)
states = ['.'] * 9
ans = 0
for i in range(n):
    for j in range(9):
        if x[i][j] == '.':
            states[j] = '.'
        elif x[i][j] == 'x':
            ans += 1
            states[j] = 'x'
        elif x[i][j] == 'o':
            if states[j] in {'.', 'x'}:
                ans += 1
            states[j] = 'o'
print(ans)
