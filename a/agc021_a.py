import sys


def input(): return sys.stdin.readline().strip()


INF = float('inf')
MOD = 10**9 + 7

# 24m + 1WA AC
n = input()
if len(n) < 2:
    print(n)

elif '9' in n and len(set(n)) == 1:
    print(sum(list(map(int, list(n)))))
elif '9' in n and len(set(n[1:])) == 1:
    print(sum(list(map(int, list(n)))))
else:
    ans = (int(n[0])-1) + 9 * len(n[1:])
    print(ans)
