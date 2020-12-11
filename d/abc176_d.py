import sys
from collections import deque


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

h, w = LI()
ch, cw = LI()
ch -= 1
cw -= 1
dh, dw = LI()
dh -= 1
dw -= 1
s = SR(h)

costs = [[INF] * w for _ in range(h)]  # costs[i][j] : マス(i, j)に到達するのに使う魔法の最小回数
costs[ch][cw] = 0
deq = deque([[ch, cw]])
while deq:
    curr_h, curr_w = deq.popleft()
    # 歩いて行けるマスを探す
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        next_h = curr_h + di
        next_w = curr_w + dj
        if not(0 <= next_h < h) or not(0 <= next_w < w):
            continue
        if s[next_h][next_w] == '#':
            continue
        # 注意：一回探索済みでも魔法より歩いていくほうがコストが小さい
        if costs[curr_h][curr_w] < costs[next_h][next_w]:
            costs[next_h][next_w] = costs[curr_h][curr_w]
            deq.appendleft([next_h, next_w])  # 両端キューの先頭に追加

    # 現在のマスから魔法 1回で向かえるマスを探す
    for next_h in range(curr_h-2, curr_h+3):
        for next_w in range(curr_w-2, curr_w+3):
            if not(0 <= next_h < h) or not(0 <= next_w < w):
                continue
            if s[next_h][next_w] == '#':
                continue
            if costs[curr_h][curr_w]+1 < costs[next_h][next_w]:
                costs[next_h][next_w] = costs[curr_h][curr_w] + 1
                deq.append([next_h, next_w])  # 両端キューの末尾に追加

ans = costs[dh][dw]
if ans == INF:
    print(-1)
else:
    print(ans)
