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
a = LI()
# i を選んで ai と ai+1の符号を入れ替える は
# x, y (x < y) を選んでax と ay の符号を入れ替える ことと同値(y - x 回 上の操作を行えばそうなる事がわかる)
cnt = [0, 0, 0]  # 正, 負, 0 の個数
for i in a:
    if i < 0:
        cnt[1] += 1
    elif i > 0:
        cnt[0] += 1
    else:
        cnt[2] += 1
if cnt[1] % 2 == 0 or cnt[2] > 0:
    ans = 0
    for i in a:
        ans += abs(i)
else:
    # 絶対値が最小の要素だけ負にする
    ans = 0
    for i in a:
        ans += abs(i)
    ans += -2 * min(abs(i) for i in a)
print(ans)
