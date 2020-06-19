# 25m AC (1WA)
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


a, b = LI()
if a == b:
    cnt = 0 if a % 4 else 1
    if a % 100 == 0 and a % 400 != 0:
        cnt = 0
    print(cnt)
    sys.exit()
elif a % 4:
    cnt = ((b - a) - (4 - (a % 4))) // 4 + 1
else:
    cnt = (b - a) // 4 + 1
# print(f'{cnt=}')
cnt -= (b // 100 - b // 400) - (a // 100 - a // 400)
# print(f'{(b // 100 - b // 400) - (a // 100 - a // 400)=}')
print(cnt)
