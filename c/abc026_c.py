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
MOD = 10**9 + 7

# 40m AC
n = I()
es = [[] for _ in range(n)]
for i in range(n-1):
    bi = I()
    bi -= 1
    es[bi].append(i+1)


salaries = [0] * n


def calc_salary(m):
    if salaries[m] != 0:
        return salaries[m]
    if not es[m]:
        return 1
    if len(es[m]) == 1:
        return 2 * calc_salary(es[m][0]) + 1
    max_s = 0
    min_s = INF
    for child in es[m]:
        max_s = max(max_s, calc_salary(child))
        min_s = min(min_s, calc_salary(child))
    return max_s + min_s + 1


print(calc_salary(0))
