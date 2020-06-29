import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def satisfaction(d, last, c):
    res = 0
    for i in range(26):
        res += c[i] * (d - last[i])
    return res


def main():
    d = I()
    c = LI()
    s = LIR(d)
    last = [0] * 26
    out = []
    satis = 0
    for day in range(d):
        # 貪欲法 : day 日目終了時点で満足度が最も大きくなるようなコンテスト k を選ぶ
        today_satises = []
        for k in range(26):
            last[k] = day + 1
            today_satises.append(s[day][k] - satisfaction(day + 1, last, c))
            last[k] -= day + 1  # もとに戻す
        satis += max(today_satises)
        contenst = today_satises.index(max(today_satises))
        last[contenst] = day + 1
        out.append(contenst + 1)

    print(*out, sep='\n')


main()
