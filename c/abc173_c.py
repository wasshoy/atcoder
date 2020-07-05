import numpy as np
from itertools import combinations
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


h, w, k = LI()
c = [list(S()) for _ in range(h)]
c = np.array(c)
# print(c)
hl = list(range(h))
wl = list(range(w))
ans = 0
for i in range(h + 1):  # i 個の行を選ぶ
    for j in range(w + 1):  # j 個の列を選ぶ
        # print(list(combinations(hl, i)))
        for choice_line in combinations(hl, i):
            for choice_col in combinations(wl, j):
                tmp_c = np.copy(c)
                # print('i', choice_line)
                # print('j', choice_col)
                for line in choice_line:
                    tmp_c[line] = 'r'
                for col in choice_col:
                    tmp_c[:, col] = 'r'
                # print(tmp_c)
                if np.sum(tmp_c == '#') == k:
                    ans += 1
print(ans)
