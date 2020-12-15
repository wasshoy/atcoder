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

# 15 WA + 45m AC


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


n = I()
if n == 1:
    print('Not Prime')
    exit()

if is_prime(n):
    ans = 'Prime'
    print(ans)
    exit()

ans = 'Not Prime'
if (n % 10) % 2 != 0 and (n % 10) != 5 and n % 3 != 0:
    ans = 'Prime'

print(ans)
