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

# 11m AC
s = S()
s = s.lower()
AKIBA = 'akihabara'
if len(s) > len(AKIBA):
    print('NO')
    exit()

d = {0: 'kih', 1: 'b', 2: 'r', 3: ''}
for i in range(2**4):
    inserted = ['a' if i >> j & 1 else '' for j in range(4)]
    res = ''
    for j in range(4):
        res += inserted[j] + d[j]
    if res == s:
        print('YES')
        exit()
print('NO')
