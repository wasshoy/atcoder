# エラトステネスのふるい : n 以下の全ての素数を列挙
# 計算量: O(N log log N)
# n 以下の素数のリストを返す
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
