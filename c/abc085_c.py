import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n, y = LI()
ans = [-1, -1, -1]
for i in range(n + 1):
    for j in range(n + 1):
        k = n - i - j
        if k < 0:
            continue

        money = 10000 * i + 5000 * j + 1000 * k
        if money == y:
            ans = [i, j, k]
            break
print(*ans)
