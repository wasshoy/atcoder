import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


# 21
h, w = LI()
s = [list(S()) for _ in range(h)]
ans = 0
# dp[i][j] : (i, j) に到達するのに操作の回数の最小値
dp = [[INF] * w for _ in range(h)]
dp[0][0] = 0 if s[0][0] == '.' else 1
for y in range(h):
    for x in range(w):
        for dy, dx in [(0, 1), (1, 0)]:
            ny = y + dy
            nx = x + dx
            if not(ny < h) or not(nx < w):
                continue
            if s[ny][nx] == '.' or (s[ny][nx] == '#' and s[y][x] == '#'):
                dp[ny][nx] = min(dp[ny][nx], dp[y][x])
            elif s[ny][nx] == '#' and s[y][x] == '.':
                dp[ny][nx] = min(dp[ny][nx], dp[y][x]+1)

print(dp[h-1][w-1])
