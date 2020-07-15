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
k, a, b = LI()

# a 枚を 1 円に交換、1 円を b 枚に交換 の 2 回の操作で b - a 枚増える
if b - a <= 2:
    print(1 + k)
    exit()

rest_k = k - (a - 1)  # 初めに a 枚になるまで増やした後の残り回数
if rest_k < 0:
    ans = 1 + k  # a 枚にすることができないならただ k 枚増やす
else:
    ans = a
    # 残りの操作回数で 可能な限り b - a 枚増やす操作を行う
    ans += (b - a) * (rest_k // 2)
    ans += rest_k % 2  # 残りが奇数回なら最後の １ 回は 1 枚増やす
print(ans)
