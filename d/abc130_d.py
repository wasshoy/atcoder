import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n, k = LI()
a = LI()
ans = 0
# kを超える最小の部分列を見つけたい
sum_ = 0
right = 0
for left in range(n):
    # 尺取り法で [left, right) の総和が k 以上となる最小の right を求める
    while right < n and sum_ < k:
        sum_ += a[right]
        right += 1

    if sum_ < k:  # もう left を進めても条件を満たさないので処理を終える
        break

    ans += n - right + 1
    sum_ -= a[left]

print(ans)
