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

n = I()
s = S()
stack = []

ans = n
for si in s:
    if stack[-2:] == ['f', 'o'] and si == 'x':
        stack.pop()
        stack.pop()
        ans -= 3
    else:
        stack.append(si)

if ''.join(stack[-3:]) == 'fox':
    ans -= 3
print(ans)
