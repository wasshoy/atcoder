import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def main():
    t = I()
    n = I()
    a = LI()
    m = I()
    b = LI()
    ans = 'yes'
    for customer in b:
        is_ok = False
        for takoyaki in a:
            if takoyaki <= customer <= takoyaki + t:
                a.remove(takoyaki)
                is_ok = True
                break
        if not is_ok:
            ans = 'no'
            break
    print(ans)


main()
