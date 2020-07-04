# 14m AC
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


n, m = LI()
ans = 0
if 2 * n <= m:
    # Sを全部使う
    ans += n
    m -= 2 * n
    n -= n
    # c のあまりで作る
    if m >= 4:
        ans += m // 4
        m -= 4 * (m // 4)
    print(ans)

else:
    ans += m // 2
    n -= m // 2
    m -= 2 * (m // 2)
    print(ans)
