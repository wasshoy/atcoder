import sys
from datetime import datetime, timedelta


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')

# datetimeモジュールを使って日付を進める

formatter = '%Y/%m/%d'
date = datetime.strptime(input(), formatter)

while True:
    y, m, d = date.year, date.month, date.day
    if y % (m*d) == 0:
        break
    date += timedelta(days=1)  # 1日進める

ans = date.strftime(formatter)
print(ans)
