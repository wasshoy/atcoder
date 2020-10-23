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


t = I()
base = 'atcoder'
for _ in range(t):
    s = S()
    set_c = set(list(s))
    if s > base:
        print(0)
        continue
    elif 'a' in set_c and len(set_c) == 1:
        print(-1)
        continue

    ans = 0
    for i, c in enumerate(s):
        if c != 'a':
            if c <= 't':  # c を先頭に移動させた場合
                ans = i
            else:  # c を先頭から2番目に移動させた場合
                ans = i - 1
            print(ans)
            break
