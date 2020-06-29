import math
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


# a, bの公約数の集合 と a, bの最大公約数の約数の集合 は同値
# a, bの最大公約数の約数のうち、互いに素なもの <= a, bの最大公約数の素因数と(と 1)
# n の素因数分解はO(√ n)で行える

# ↑の方法とは異なる解法
def prime_factrize(n: int) -> list:
    # 素因数のリストを取得(重複する素因数を含む)
    # 例 : 18 -> [2, 3, 3]
    if n < 2:
        return []
    p_factors = []
    # 2だけ先に取り分けておく
    while n % 2 == 0:
        p_factors.append(2)
        n //= 2
    # 残りの奇数の素因数を探す
    f = 3
    while f * f <= n:
        if n % f == 0:
            p_factors.append(f)
            n //= f
        else:
            f += 2
    # nが素数の場合
    if n != 1:
        p_factors.append(n)
    return p_factors


def main():
    a, b = LI()
    # a, bの素因数を取り出し、共通する素因数(に1を加えたもの)の個数を数える
    pf_a = prime_factrize(a)
    pf_b = prime_factrize(b)
    pf = (set(pf_a) & set(pf_b)) | {1}
    print(len(pf))


main()
