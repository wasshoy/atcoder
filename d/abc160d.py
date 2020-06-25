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


def main():
    n, x, y = LI()
    x, y = x - 1, y - 1
    d = [[INF] * n for _ in range(n)]
    ans = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            d[i][j] = min([j - i,
                           abs(x - i) + 1 + abs(j - y),
                           abs(y - i) + 1 + abs(j - x)])
            ans[int(d[i][j])] += 1
    print(*ans[1:], sep='\n')


main()
