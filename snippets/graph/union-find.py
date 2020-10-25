from collections import Counter
import sys


def input(): return sys.stdin.readline().strip()
def LI(): return list(map(int, input().split()))


n, m = LI()
parents = [i for i in range(n)]


def root(x):
    if parents[x] == x:
        return x
    else:
        return root(parents[x])


def unite(x, y):
    root_x = root(x)
    root_y = root(y)
    if root_x == root_y:
        return
    parents[root_x] = parents[root_y]


def same(x, y):
    return root(x) == root(y)


for _ in range(m):
    a, b = LI()
    a -= 1
    b -= 1
    unite(a, b)


print(parents)
c = Counter(parents)
ans = max(c.values())
print(ans)
