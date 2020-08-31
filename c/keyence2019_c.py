# 13
import sys
import numpy as np


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
a = np.array(LI())
b = np.array(LI())
diff = a - b
pos = [diff[i] for i in range(len(diff)) if diff[i] > 0]
neg = [diff[i] for i in range(len(diff)) if diff[i] < 0]
if sum(pos) + sum(neg) < 0:
    print(-1)
    exit()

# if len(neg) == 0:
#     print(0)
#     exit()

ans = len(neg)
s_neg = sum(neg)
sort_pos = sorted(pos)[::-1]
for elem in sort_pos:
    if s_neg < 0:
        ans += 1
        s_neg += elem
    else:
        break
print(ans)
