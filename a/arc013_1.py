import sys
from itertools import permutations


def input(): return sys.stdin.readline().strip()


n, m, l = map(int, input().split())
nimotsu = list(map(int, input().split()))
ans = 0
# ダンボールの各辺に荷物の各辺を割り当てる
for i, j, k in permutations([i for i in range(3)]):
    ans = max(ans, (n//nimotsu[i]) * (m//nimotsu[j]) * (l//nimotsu[k]))
print(ans)
