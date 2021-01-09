import sys
from collections import Counter


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# 15
# 8の倍数: 下3桁が8の倍数
# 下三桁 / 2 が4の倍数
s = S()
if len(s) == 1:
    if s == '8':
        print('Yes')
    else:
        print('No')
    exit()

if len(s) == 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

counter = Counter(s)
for i in range(13, 125):
    icounter = Counter(str(i*8))
    if not icounter - counter:
        print('Yes')
        exit()
print('No')
