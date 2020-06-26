import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


x = I()
# xの最大値が 10^ 9
# xの最大値となるa, bを考える
# xがより大きくなるのは a^5とb^5 の差が小さい(0ではない)とき
# a と b の差が 1 のとき差が最も小さい
# この場合で xが10^9をギリギリ越さない a, bを考える
# a, bが0以上の場合
# a = 120, b = 119のときがギリギリ
# a, bが0以下の場合
# a = -118, b = -119のときギリギリ
# a は [-118, 121], b は [-119, 119]の範囲で探索
a = list(range(-118, 121))
b = list(range(-119, 120))
ans = [-118, -119]
for i in a:
    for j in b:
        if i ** 5 - j ** 5 == x:
            ans = [i, j]
            break
print(*ans)
