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

# 35m + 3WA AC
y, m, d = map(int, input().split('/'))
for year in range(y, 3001):
    start_month = m if year == y else 1
    for month in range(start_month, 13):
        start_day = d if year == y and month == m else 1
        last_day = 30 if month in {4, 6, 9, 11} else 29 if month == 2 and (
            year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28 if month == 2 else 31
        for day in range(start_day, last_day+1):
            if year % (month*day) == 0:
                m_s = str(month)
                d_s = str(day)
                if month//10 < 1:
                    m_s = '0' + m_s
                if day//10 < 1:
                    d_s = '0' + d_s
                ans = '/'.join((str(year), m_s, d_s))
                print(ans)
                exit()
