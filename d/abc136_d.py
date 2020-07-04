# 50m AC
from collections import defaultdict
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
n = len(s)
d = defaultdict(lambda: [0, 0])  # RL の位置 に対応する r, l の数の辞書

# 右から見ていって対応する r を探す
r = 0
i = 0
while i < n:
    if s[i:i + 2] == 'RL':
        d[i][0] = r
        r = 0
        i += 2
    elif s[i] == 'R':
        r += 1
        i += 1
    else:
        i += 1

l = 0
i = 0
s = s[::-1]
while i < n:
    if s[i:i + 2] == 'LR':
        d[n - i - 2][1] = l
        l = 0
        i += 2
    elif s[i] == 'L':
        l += 1
        i += 1
    else:
        i += 1


ans = [0] * n
for k, v in d.items():
    r, l = v
    ans[k] += 1
    ans[k + 1] += 1
    if r % 2 == 0:
        ans[k] += r // 2
        ans[k + 1] += r // 2
    else:
        ans[k] += r // 2
        ans[k + 1] += r // 2 + 1
    if l % 2 == 0:
        ans[k] += l // 2
        ans[k + 1] += l // 2
    else:
        ans[k] += l // 2 + 1
        ans[k + 1] += l // 2
print(*ans)
