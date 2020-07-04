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
# 区間スケジューリング問題 : いくつかの区間の中から重ならないように最大で何個選べるか
# ソート + 貪欲法 で解ける
# なるべく多くの数を並べたい -> 短いものを選んでいけば良さそう？
arm_pos = []
for _ in range(n):
    x, l = LI()
    arm_pos.append([x - l, x + l])
arm_pos = sorted(arm_pos, key=lambda x: x[1])  # アームの終点の位置でソート
ans = n
for i in range(n - 1):
    if arm_pos[i][1] > arm_pos[i + 1][0]:  # i のアームの終点が i + 1 のアームの始点 と重なっていた場合
        arm_pos[i + 1] = arm_pos[i]  # i + 1 のアームを取り除く
        ans -= 1
print(ans)
