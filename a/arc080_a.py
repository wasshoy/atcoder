# 30m弱くらい? AC
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
a = LI()
cnt_4 = len([True for elem in a if elem % 4 == 0])
if cnt_4 >= n // 2:
    print('Yes')
    sys.exit()
rest = n - cnt_4 * 2
cnt_2 = len([True for elem in a if elem % 2 == 0 and elem % 4 != 0])
if rest == 1:
    print('Yes')
elif cnt_2 == rest:
    print('Yes')
else:
    print('No')
