import sys


def input(): return sys.stdin.readline().strip()


INF = float('inf')
MOD = 10**9 + 7

# 11m AC
b = list(map(int, input().split()))
n = int(input())
a = [int(input()) for _ in range(n)]
d = {v: i for i, v in enumerate(b)}
changed = []
for elem in a:
    if elem//10 == 0:
        changed.append((d[elem], elem))
    else:
        num = ''
        for i in str(elem):
            num += str(d[int(i)])
        num = int(num)
        changed.append((num, elem))
changed.sort(key=lambda x: x[0])
for elem in changed:
    print(elem[1])
