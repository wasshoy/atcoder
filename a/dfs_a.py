import sys
sys.setrecursionlimit(10**7)


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
c = [list(S()) for _ in range(h)]
start_h, start_w = 0, 0
goal_h, goal_w = 0, 0
for i in range(h):
    for j in range(w):
        if c[i][j] == 's':
            start_h = i
            start_w = j
        if c[i][j] == 'g':
            goal_h = i
            goal_w = j

is_seen = [[False] * w for _ in range(h)]


def dfs(sh, sw):
    if not(0 <= sh < h) or not(0 <= sw < w):
        return
    if c[sh][sw] == '#' or is_seen[sh][sw]:
        return
    if c[sh][sw] == 'g':
        print('Yes')
        exit()
    is_seen[sh][sw] = True
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh = sh + dh
        nw = sw + dw
        dfs(nh, nw)


dfs(start_h, start_w)
print('No')
