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


def calc_cumsum(l):
    cumsum = [0]
    for i in l:
        cumsum.append(cumsum[-1] + i)
    return cumsum


n, q = LI()
lr = LIR(q)
# いもす法 を使って O(q + n) で解く
# それぞれの裏返しの回数を計算したい
komas = [0] * n   # r = n のときの r + 1 ために余分に準備
# 1. 加算処理
for l, r in lr:
    l, r = l - 1, r - 1
    komas[l] += 1
    if r + 1 < n:
        komas[r + 1] -= 1

# 2. 累積和
cumsum = calc_cumsum(komas)[1:]  # 返された回数になる
ans = ''
for masu in cumsum:
    if masu % 2 == 0:
        ans += '0'
    else:
        ans += '1'
print(ans)
