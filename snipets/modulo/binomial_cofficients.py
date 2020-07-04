# nCr (mod p) を O(n) で求める


# nCr : 二項係数という

# 二項係数の総和 r = 0 ~ n に関する nCr の和
def sum_n_c_r(n, r):
    return 2 ** n
# これは二項定理より証明可能


# nCr = n! / ((n - r)! × r!) を愚直に計算するのは n が大きいとつれえわ(mod_practice.py で for 文による愚直な計算を実装)
# math.factorial を使っても同様に求められるがとて同じこと
# 1. n! と 1 / (n - r)! と 1 / r! について 掛け合わせる前に mod p を計算しておく
# 2. それらをかけ合わせる

# O(n)で計算
# nCr mod p を 返す
def n_c_r(n, r, p):
    fact_mod = [1, 1]  # fact_mod[i] : i! mod p
    fact_inv_mod = [1, 1]  # fact_inv_mod[i] : 1 / i! mod p (逆元)
    inv = [0, 1]  # fact_inv_mod の計算用 inv[i] : i の逆元 i^(-1)
    # 階乗の計算
    for i in range(2, n + 1):
        fact_mod.append(fact_mod[-1] * i % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        fact_inv_mod.append((fact_inv_mod[-1] * inv[-1]) % p)
    return fact_mod[n] * fact_inv_mod[r] * fact_inv_mod[n - r] % p

    # 解説
    # fact_mod には 単純に 1 に 2 から n を掛けながら随時 mod p をとっている
    # fact_inv_mod の計算はちょっとややこしい
    # 1 / n! =  i = 1 ~ n の範囲で 1 / i を総乗(Π)したもの と書ける
    # つまり、 1 / i は逆元なので逆元を掛けていけば求められる
    # a ^ (-1) ≡ x mod p を満たす 整数 x をモジュラ逆数 という
    # モジュラ逆数は以下の性質を持つ
    # a ^ (-1) ≡ -(p % a)^(-1) × (p // a)  mod p
    # (モジュラ逆数の性質などの証明などは割愛)
    # これにより i の逆元を計算して求めて掛けていく
    # 随時 mod p を取ることも忘れずに
    # 参考 https://www.planeta.tokyo/entry/5195/


if __name__ == '__main__':
    n = 10 ** 6
    r = 10 ** 4
    p = 10 ** 9 + 7
    print(n_c_r(n, r, p))
