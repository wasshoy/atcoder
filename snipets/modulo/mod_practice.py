
def mod_basic():
    mod = 10 ** 9 + 7
    a = 111111111
    b = 123456789
    c = 987654321
    # かけ算 ： 途中で余りをとっても良い
    print(f'{a * b * c % mod=}')
    print(f'{a * b % mod * c % mod=}')
    # 引き算 ： Pythonでは負の数も上手く結果を返してくれるので、たし算と同じ扱いで良い
    print(f'{(a - b) % mod=}')
    print(f'{(a % mod - b % mod) % mod=}')
    # 割り算
    # 1 ÷ b (b の逆元) を求める必要がある
    # mod m における a の逆元 a^{-1} を計算する


# Fermat の小定理 を 用いる方法 ( O(m) バージョン)
# m が素数である必要がある
# pow(x, y, m) : x ^ y (mod p) を返す
def modinv(a, m): return pow(a, m - 2, m)


# 拡張 Euclid 互除法を利用する方法
# m が素数である必要がない
# O(log m)

# 拡張ユークリッドの互除法
# 互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0] - q * w[0], r[1] - q * w[1], r[2] - q * w[2]]
        r = r2
        w = w2
    # [x,y]
    return [w[0], w[1]]


# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m


def main():
    mod = 10 ** 9 + 7

    a = 12345678900000
    b = 100000
    print(mod_inv(a, mod))
    print((a % mod) * mod_inv(b, mod) % mod)

    # nCk mod 10 ** 9 + 7 の具体例
    # nCk = n! / ((n - k)! * k!)
    # n!, (n - k)!, k! のそれぞれを逆元を利用計算していく
    res = 1
    # n = 10000, k = 4000
    n = 10000
    k = 4000
    for i in range(1, n + 1):
        res = res * i % mod
    for i in range(1, k + 1):
        res = res * mod_inv(i, mod) % mod
    for i in range(1, n - k + 1):
        res = res * mod_inv(i, mod) % mod
    print(f'{res=}')

    # 16 / 4 ≡ 1 * 4 ≡ 4 ≡ 1 (mod 3)
    print(mod_inv(4, 3))
    print((16 % 3) * mod_inv(4, 3) % 3)

    # 28 / 4 ≡ 3 * 4 ≡ 12 ≡ 2 (mod 5)
    print(mod_inv(4, 5))
    print((28 % 5)*mod_inv(4, 5) % 5)

    # 45 / 5 ≡ 0 * 2 ≡ 0 (mod 3)
    print(mod_inv(5, 3))
    print((45 % 3)*mod_inv(5, 3) % 3)

    # 54 / 7 ≡ 2 * 3 ≡ 6 ≡ 2 (mod 4)
    print(mod_inv(7, 4))
    print((54 % 4)*mod_inv(7, 4) % 4)

    # 400 / 4 / 5 ≡ 1 * 2 * 3 ≡ 6 (mod 7)
    print(mod_inv(4, 7))
    print(mod_inv(5, 7))
    print((400 % 7)*mod_inv(4, 7)*mod_inv(5, 7) % 7)


main()
