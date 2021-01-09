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
ans = 0
a_inds = set()
b_inds = set()
ab_inds = set()
for i in range(n):
    si = S()
    if si[-1] == 'A':
        a_inds.add(i)
    if si[0] == 'B':
        b_inds.add(i)
    if si[-1] == 'A' and si[0] == 'B':
        ab_inds.add(i)
    for j in range(len(si)-1):
        if si[j:j+2] == 'AB':
            ans += 1
a_only = a_inds - ab_inds
b_only = b_inds - ab_inds
if not ab_inds:
    ans += min(len(a_only), len(b_only))
else:
    if a_only or b_only:
        ans += len(ab_inds) + min(len(a_only), len(b_only))
    else:
        ans += len(ab_inds) - 1
print(ans)
