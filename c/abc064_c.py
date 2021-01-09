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
a = LI()
color = [0] * 9
for ai in a:
    color[min(ai//400, 8)] += 1

type_num = len([i for i in color[:-1] if i > 0])

if type_num == 0:
    min_ans = 1
else:
    min_ans = type_num

max_ans = type_num + color[-1]
print(min_ans, max_ans)
