import sys
# フィボナッチ数列を計算する
# 漸化式通り


def fib_base(n):
    if n <= 1:
        return n
    return fib_base(n - 2) + fib_base(n - 1)


# メモ化
def fib_memo(n):
    memo = [-1] * (n + 1)

    def _fib(n):
        if n <= 1:
            return n
        if memo[n] != -1:
            return memo[n]
        memo[n] = _fib(n - 2) + _fib(n - 1)
        return memo[n]

    return _fib(n)


# dp
def fib_dp(n):
    dp = [-1] * (n + 1)
    if n <= 1:
        return n
    dp[0] = 0
    dp[1] = 1

    def _fib(n):
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]
    return _fib(n)


n = int(sys.argv[1])
print(fib_base(n))
print(fib_memo(n))
print(fib_dp(n))
