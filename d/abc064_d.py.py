import sys
from collections import Counter, deque


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


# 30m AC
n = I()
s = S()
ans = s[:]
stack = deque([])
for bracket in s:
    if bracket == '(':
        stack.append(bracket)
    else:
        if len(stack) != 0:
            stack.pop()
        else:  # 現時点で左括弧が足りない
            ans = '(' + ans
ans = ans + ')' * len(stack)  # 右括弧が足りない
print(ans)
