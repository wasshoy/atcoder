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

n, m = LI()
a = LI()
if m == 0:
    print(1)
    exit()
a = list(map(lambda x: x-1, a))  # 0-indexed
a.sort()
# print(a)
# 白色の連続個数を調べる
white = []
if a[0] != 0:  # 先頭が白色から始まる場合
    white.append(a[0])

for i in range(len(a)-1):
    if a[i+1]-a[i]-1 > 0:
        white.append(a[i+1] - a[i] - 1)
if a[-1] != n-1 and (n-1) - a[-1] - 1 > 0:  # 末尾が青色出ない場合
    white.append(n-a[-1]-1)

if len(white) == 0:
    print(0)
    exit()

# print(white)
k = min(white)
ans = 0
for wi in white:
    if wi % k == 0:
        ans += wi // k
    else:
        ans += wi//k + 1
print(ans)
