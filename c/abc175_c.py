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

# 13
X, K, D = LI()
X = abs(X)

# 0 を通り越さない場合
if D*K <= X:
    print(X - D*K)

# 0 を通り越す場合 D*K > X
else:
    # 0 を通り越す直前座標まで来たときの残り回数
    rest = K - X//D
    if rest % 2 == 0:
        print(X % D)
    else:
        print(abs(X % D - D))
