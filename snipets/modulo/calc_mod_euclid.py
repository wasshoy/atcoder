# mod m における a の逆元を O(log m) で計算

# 拡張 Euclid 互除法を利用する方法
# m が素数である必要がない

# 拡張ユークリッドの互除法
# 互いに素なa,bについて、a*x+b*y=1の一つの解 を求める

# aの逆元(mod m)を求める(aとmは互いに素であることが前提)
# 余りは O(log m) で計算


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


# mod m における a の逆元を返す
def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m + x % m) % m
