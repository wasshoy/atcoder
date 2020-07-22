# 28m AC 1TLE 1WA
from collections import Counter
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
d = LI()
m = I()
t = LI()
d.sort()
t.sort()
c_t = Counter(t)
c_d = Counter(d)
# print(c_t.items())
# print(c_d.items())
ans = 'YES'
i = 0
c_d = dict([(k, v) for k, v in c_d.items() if k in c_t.keys()])
if len(c_d) != len(c_t):
    ans = 'NO'
    print(ans)
    exit()
for (k_t, v_t), (k_d, v_d) in zip(c_t.items(), c_d.items()):
    if v_t > v_d:
        ans = 'NO'
        break
print(ans)
