# 10m AC
import math
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


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def f(a, b):
    return max(len(str(a)), len(str(b)))


n = I()
divs = make_divisors(n)
divs = [elem for elem in divs if elem <= math.sqrt(n)]
ans = f(divs[0], n // divs[0])
for i in divs:
    ans = min(ans, f(i, n // i))
print(ans)
