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
a = LI()
left = [i + ai for i, ai in enumerate(a, start=1)]
right = [j - aj for j, aj in enumerate(a, start=1)]
r_counter = Counter(right)
ans = 0
for l in left:
    ans += r_counter[l]
print(ans)
