# 20 ~ 25m AC
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


x, y, a, b, c = LI()
p = sorted(LI())[::-1][:x]
q = sorted(LI())[::-1][:y]
r = sorted(LI())[::-1][:x+y]
# print(p, q, r)
bucket = []
bucket += [[i, 'p'] for i in p]
bucket += [[i, 'q'] for i in q]
bucket += [[i, 'r'] for i in r]
bucket = sorted(bucket, key=lambda x: x[0])
# print(bucket)
d = {'p': 0, 'q': 0}
ans = 0
cnt = 0
while cnt < x + y:
    if bucket[-1][1] == 'p' and d[bucket[-1][1]] < x:
        ans += bucket.pop()[0]
        d['p'] += 1
        cnt += 1
    elif bucket[-1][1] == 'q' and d[bucket[-1][1]] < y:
        ans += bucket.pop()[0]
        d['q'] += 1
        cnt += 1
    else:
        ans += bucket.pop()[0]
        cnt += 1
print(ans)
