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


def f(m):
    res = 0
    r_m = math.sqrt(m)
    for i in range(1, int(r_m) + 1):
        for j in range(1, int(r_m) + 1):
            for k in range(1, int(r_m) + 1):
                if i ** 2 + j ** 2 + k ** 2 + i * j + j * k + k * i == m:
                    print(f'{(m, i, j, k)=}')
                    res += 1
    return res


n = I()
cnt = [0] * 10001
r_n = int(math.sqrt(n)) + 1
for x in range(1, r_n):
    for y in range(1, r_n):
        for z in range(1, r_n):
            v = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if v <= n:
                cnt[v] += 1

for i in range(1, n + 1):
    print(cnt[i])
