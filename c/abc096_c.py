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

# 20m AC
h, w = LI()
s = SR(h)
for i in range(h):
    for j in range(w):
        is_ok = False
        if s[i][j] == '.':
            continue
        else:
            # 上下左右に黒が1つも隣接していなければ不可能
            if 0 < i:
                if s[i-1][j] == '#':
                    is_ok = True
            if i < h-1:
                if s[i+1][j] == '#':
                    is_ok = True
            if 0 < j:
                if s[i][j-1] == '#':
                    is_ok = True
            if j < w-1:
                if s[i][j+1] == '#':
                    is_ok = True

        if not is_ok:
            print('No')
            exit()
print('Yes')
