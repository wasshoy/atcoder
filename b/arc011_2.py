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

# 57
n = I()
w = LS()
igored = {'a', 'i', 'u', 'e', 'o', 'y', '.', ','}
d = [
    [{'b', 'c'}, 1],
    [{'d', 'w'}, 2],
    [{'t', 'j'}, 3],
    [{'f', 'q'}, 4],
    [{'l', 'v'}, 5],
    [{'s', 'x'}, 6],
    [{'p', 'm'}, 7],
    [{'h', 'k'}, 8],
    [{'n', 'g'}, 9],
    [{'z', 'r'}, 0],
]
ans = []
for wi in w:
    res = ''
    for c in wi:
        c = c.lower()
        if c in igored:
            continue
        for ks, v in d:
            if c in ks:
                res += str(v)
    if res:
        ans.append(res)
print(' '.join(ans))
