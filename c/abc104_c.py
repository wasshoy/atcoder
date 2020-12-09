import sys
from itertools import product


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

d, g = LI()
p = []
c = []
for _ in range(d):
    pi, ci = LI()
    p.append(pi)
    c.append(ci)

# bit全探索 + 貪欲法
# ボーナスがない場合 ： 得点が高い順に解いていけば良い
# ボーナスがある場合 ： ある配点の問題を全て解くか・解かないかを考え、
# Gに届かない場合は得点が高い順に解いていけば良い

ans = sum(p)
for bits in product((False, True), repeat=d):  # 全て解くか・解かないか
    score = sum([(100*(i+1)) * p[i] for i, bit in enumerate(bits) if bit])
    solved = [True if bit else False for bit in bits]
    cnt = sum([p[i] for i, bit in enumerate(bits) if bit])
    for i, bit in enumerate(bits):
        if bit:
            score += c[i]

    if score >= g:
        ans = min(ans, cnt)

    else:  # 残りの問題で得点が高い順に 1 問ずつ解いていく
        for i in reversed(range(d)):
            if solved[i]:
                continue

            is_ok = False
            for j in range(1, p[i]+1):
                score += 100*(i+1)
                cnt += 1

                if score >= g:
                    is_ok = True
                    break
            if is_ok:
                ans = min(ans, cnt)
print(ans)
