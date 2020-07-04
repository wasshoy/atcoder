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


nums = list(map(int, S()))
ans = ''
for i in range(2 ** 3):
    res = nums[0]
    ans = str(nums[0])
    for j in range(3):
        if i >> j & 1:
            res += nums[j + 1]
            ans += f'+{nums[j + 1]}'
        else:
            res -= nums[j + 1]
            ans += f'-{nums[j + 1]}'
    if res == 7:
        ans += '=7'
        break
print(ans)
