# 素因数分解 O(√N)
# 試し割り法
# nより小さい数で順に割っていき割り切れるかどうかで素因数の判定を行う
# 素因数が見つかった場合、その素因数で割り切れなくなるまでnを更新する
# Nの素因数は最大でも√NであることよりO(√N)で計算可能
# (素因数とその個数はcollections のCounterを使うと手軽)

from collections import Counter


def prime_factrize(n):
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


# 素因数とその個数のタプルのリストを返す
def get_prime_counts(n):
    p_factors = prime_factrize(n)
    counter = Counter(p_factors)
    return list(counter.items())
