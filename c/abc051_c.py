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
MOD = 10**9 + 7

# 1WA + 45m AC
sx, sy, tx, ty = LI()
# スタートを原点にずらす
tx, ty = tx - sx, ty - sy
res = ty*'U' + tx*'R'
res += ty*'D' + tx*'L'
res += 'L' + ty*'U' + 'U' + 'R' + tx*'R' + 'D'
res += 'R' + ty*'D' + 'D' + 'L' + tx*'L' + 'U'
print(res)
