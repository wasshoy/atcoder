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
MOD = 10**9 + 7

n = I()
s = SR(n)
set1 = set()
set2 = set()
for si in s:
    if si[0] == '!':
        set2.add(si[1:])
    else:
        set1.add(si)

ans_set = set1 & set2
if len(ans_set) != 0:
    print(ans_set.pop())
else:
    print('satisfiable')
