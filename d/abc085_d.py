import sys
import numpy as np


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

# 3WA + 65m AC
n, h = LI()
a = []
b = []
for _ in range(n):
    ai, bi = LI()
    a.append(ai)
    b.append(bi)

a_sort_i = np.argsort(a)[::-1]
main_sword_i = a_sort_i[0]  # 振るダメージが最も大きい刀
for i in a_sort_i:
    # 振るダメージが最も高く、振るダメージが同じなら、投げるダメージがなるべく小さいものを振る刀に選ぶ
    if a[i] == a[main_sword_i] and b[i] < b[main_sword_i]:
        main_sword_i = i

# 投げると、振るの最大ダメージよりダメージが出せる刀を先に投げる
throw_swords = []
for i in range(n):
    if i == main_sword_i:
        continue
    if b[i] > a[main_sword_i]:
        throw_swords.append(b[i])
throw_swords.sort(reverse=True)

ans = 0
# 振る刀を1回投げて倒せるかどうか
if b[main_sword_i] >= h:
    print(1)
    exit()

# ダメージが大きい順に刀を投げていく
for s in throw_swords:
    h -= s
    ans += 1
    if h <= 0:
        print(ans)
        exit()

# 刀を振る
ans += 1
h -= b[main_sword_i]  # 最後は投げるので先に計算
if h <= 0:
    print(ans)
    exit()
ans += h // a[main_sword_i]
h %= a[main_sword_i]
if h > 0:
    ans += 1
print(ans)
