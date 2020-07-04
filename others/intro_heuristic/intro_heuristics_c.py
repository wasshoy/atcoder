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
    D = I()
    c = LI()
    s = LIR(D)
    t = IR(D)
    m = I()
    dq = LIR(m)

    last = [0] * 26
    sats = 0
    for day in range(D):
        j = t[day] - 1
        last[j] = day + 1
        sats += s[day][j] - satisfaction(day + 1, last, c)

    for d, q in dq:
        last_2 = [0] * 26
        d -= 1
        old = t[d]
        t[d] = q
        current_sats = 0
        for day in range(D):
            j = t[day] - 1
            last_2[j] = day + 1
            current_sats += s[day][j] - satisfaction(day + 1, last, c)
        if current_sats <= sats:
            t[d] = old
            print(sats)
        else:
            print(current_sats)


main()
