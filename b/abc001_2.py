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

# 18m AC
m = I()
if m < 100:
    print('00')
elif m <= 5000:
    vv = 10*m // 1000
    if len(str(vv)) == 1:
        vv = '0' + str(vv)
    print(vv)
elif m <= 30000:
    vv = m//1000 + 50
    print(vv)
elif m <= 70000:
    km = m // 1000
    vv = ((km-30)//5) + 80
    print(vv)
else:
    print(89)
