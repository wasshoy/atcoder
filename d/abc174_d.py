from collections import Counter
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
c = S()
# 最終的に RR...RWW...WWW という状態になる
# R の個数を r とすると、左から r 個の石のうち R はそのままで W だけ入れ替えたら良い
r = Counter(list(c))['R']
ans = 0
for elem in c[:r]:
    if elem == 'W':
        ans += 1
print(ans)
