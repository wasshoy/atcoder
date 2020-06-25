import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


a, b, x = LI()
acnt = (a - 1) // x if a > 0 else -1
bcnt = b // x if b != 0 else 1
ans = bcnt - acnt if not(a == b == 0) else 1
print(ans)
