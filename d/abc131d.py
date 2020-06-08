import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
ab = [LI() for _ in range(n)]
ab_s = sorted(ab, key=lambda x: x[1])
coll_t = 0
ans = 'Yes'
for a, b in ab_s:
    coll_t += a
    if coll_t > b:
        ans = 'No'
        break

print(ans)
