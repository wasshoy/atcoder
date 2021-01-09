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

# 13m AC
n = I()
n -= 1
team_nums = []
nums = list(range(20))
for _ in range(10):
    team_nums += nums
    nums = nums[::-1]
print(team_nums[n]+1)
