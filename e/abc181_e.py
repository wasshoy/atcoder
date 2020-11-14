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

# 58
n, m = LI()
h = LI()
w = LI()
h.sort()
w.sort()

l = [0] * (n+10)
r = [0] * (n+10)

l_sum = 0
for i in range(n):
    if(i * 2 + 1 >= n):
        break
    l_sum += h[2*i+1] - h[2*i]
    l[i * 2 + 1] = l_sum

r_sum = 0
for i in range(n):
    if(i * 2 + 1 >= n):
        break
    r_sum += h[n - 1 - i*2] - h[n-1-i*2-1]
    r[n-1-i*2-1] = r_sum

ans = INF
p = 0
for wi in w:
    while p < n and h[p] < wi:
        p += 1
    if p % 2 == 0:
        ans = min(ans, l[p-1] + abs(h[p] - wi) + r[p+1])
    else:
        ans = min(ans, l[p-2] + abs(h[p-1] - wi) + r[p])
print(ans)
