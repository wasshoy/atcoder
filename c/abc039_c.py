# 6WA やべ〜
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

s = S()
base = 'WBWBWWBWBWBW' + 'WBWBWWBWBWBW' + 'WBWBWWBWBWBW'
anses = {0: 'Do', 2: 'Re', 4: 'Mi', 5: 'Fa', 7: 'So', 9: 'La', 11: 'Si'}
ans = ''
for i in [0, 2, 4, 5, 7, 9, 11]:
    if s == base[i:i + 20]:
        ans = anses[i]
        break
print(ans)
