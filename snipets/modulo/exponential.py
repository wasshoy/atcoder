# べき乗を O(log n)で計算するアルゴリズム
# Python は pow で同様の計算を行える
# 素因数分解っぽい感じ？

def exp_n(x, n):
    ans = 1
    while n:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1
    return ans


print(exp_n(2, 3))
