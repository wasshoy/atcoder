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
MOD = 10 ** 9 + 7

n, k = LI()
a = LI()
a = sorted(a, key=lambda x: abs(x))[::-1]
# print(a)
neg = [i for i in a if i < 0][::-1]
pos = [i for i in a if i >= 0]
ans = 1
if len(pos) == 0:
    if k % 2 == 0:
        for elem in neg[:k]:
            ans = ans * elem % MOD
    else:
        for elem in neg[::-1][:k]:
            ans = ans * elem % MOD
    print(ans)
else:
    for elem in a[:k]:
        ans = ans * elem % MOD
    if ans < 0:  # 非負にした上でなるべく大きな数になるようにする
        # 取り除く要素の絶対値は小さく、加える要素の絶対値は大きく
        elems = a[:k]
        neg = [i for i in elems if i < 0][::-1]
        pos = [i for i in elems if i > 0]
        # 負の数を取り除いて正の数を加える
        elems = neg[:-1] + pos[:1]
        ans_1 = 1
        for elem in elems:
            ans_1 = ans_1 * elem % MOD
        # 正の数を取り除いて負の数を加える
        ans_2 = 1
        elemes = neg[-2:-1] + pos[:-1]
        for elem in elems:
            ans_2 = ans_2 * elem % MOD
        ans = max(ans_1, ans_2)

    print(ans)
