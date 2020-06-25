from collections import defaultdict
import math
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n, m = LI()
name = S()
kit = S()
name_d = defaultdict(int)
kit_d = defaultdict(int)
for c in name:
    name_d[c] += 1
for c in kit:
    kit_d[c] += 1

ans = 0
for name_k, name_v in name_d.items():
    if name_k not in set(kit_d.keys()):
        ans = -1
        break
    ans = max(ans, math.ceil(name_v / kit_d[name_k]))

print(ans)
