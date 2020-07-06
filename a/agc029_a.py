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
ans = 0
w_cnt = 0
for i in range(len(s)):
    if s[i] == "W":
        ans += i - w_cnt  # その W の場所までにあった B の数
        w_cnt += 1

print(ans)
