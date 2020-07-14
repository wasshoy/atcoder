# 8
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


s = S()
alps = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ans = -1
set_s = set(list(s))
# s の長さが 26 未満のとき
# 辞書順で s 以降の単語を探す
for c in alps:
    if c not in set_s:
        ans = s + c
        print(ans)
        break
# s の長さが 26 のとき
else:
    for i in reversed(range(len(s))):
        # i - 1 文字目までの s の アルファベットの集合
        set_now_s = set(list(s[:i]))
        for c in alps:
            if c > s[i] and c not in set_now_s:
                ans = s[:i] + c
                print(ans)
                exit()
    else:
        print(-1)
