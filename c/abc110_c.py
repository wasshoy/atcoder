import sys
from collections import defaultdict
from sys import addaudithook


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


# 10

def calc_rle_l(s):
    '''要素が [文字, 文字数] の リストをかえす'''
    now_c = s[0]
    cnt = 1
    res = []
    for i in range(1, len(s)):
        if now_c == s[i]:
            cnt += 1
        else:
            res.append([now_c, cnt])
            now_c = s[i]
            cnt = 1
    res.append([now_c, cnt])
    return res


s = S()
t = S()
s_to_t = defaultdict()
t_to_s = defaultdict()
for si, ti in zip(s, t):
    if si not in s_to_t:
        s_to_t[si] = ti
    else:  # 既に対応するアルファベットが存在しているとき
        if s_to_t[si] != ti:
            print('No')
            exit()

    if ti not in t_to_s:
        t_to_s[ti] = si
    else:
        if t_to_s[ti] != si:
            print('No')
            exit()
else:
    print('Yes')
