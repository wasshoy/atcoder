import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


MOD = 10 ** 9 + 7


def calc_cumsum(l):
    cumsum = [l[0]]
    for i in l[1:]:
        cumsum.append(cumsum[-1] + i)
    return cumsum


n, k = LI()
nums = list(range(n + 1))
ans = 0
ruiseki_min = calc_cumsum(nums)
ruiseki_max = calc_cumsum(nums[::-1])
for i in range(k, n + 2):
    min_sum = ruiseki_min[i - 1]
    max_sum = ruiseki_max[i - 1]
    ans += max_sum - min_sum + 1
    ans %= MOD
print(ans)
