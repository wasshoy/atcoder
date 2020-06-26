import math
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))


# a, bの公約数の集合 と a, bの最大公約数の約数の集合 は同値
# a, bの最大公約数の約数のうち、互いに素なもの <= a, bの最大公約数の素因数と(と 1)
# n の素因数分解はO(√ n)で行える


def get_primes(n):
    root_n = int(n ** 0.5)
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, root_n + 1):
        if not is_prime[i]:
            continue
        # i の倍数の素数判定をFalseにする
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


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
    gcd = math.gcd(a, b)
    pf = prime_factrize(gcd)
    pf = set(pf)  # 素因数だけ取り出す
    # 1 を加える
    pf.add(1)
    print(len(pf))


main()
