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

# 2WA + 23m AC
n, m = LI()
d = {i: -i for i in range(1, n+1)}  # スレッドが最後に書き込まれた順番
for i in range(1, m+1):
    ai = I()
    d[ai] = i
ans = sorted(d.items(), key=lambda x: -x[1])  # 遅く書き込まれた順に並び替え
for i in range(n):
    print(ans[i][0])
