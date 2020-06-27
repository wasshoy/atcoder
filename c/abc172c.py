import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def calc_cumsum(l):
    cumsum = [l[0]]
    for i in l[1:]:
        cumsum.append(cumsum[-1] + i)
    return cumsum


def main():
    n, m, k = LI()
    a = LI()
    b = LI()
    costs = [float('inf')] * (n + m + 1)
    costs[0] = 0
    # a, b を i 冊読むのにかかる時間の累積
    ruiseki_a = [0] + calc_cumsum(a)
    ruiseki_b = [0] + calc_cumsum(b)
    best_b_num = 0  # 所要時間 k 以下で読める b の冊数の最大値
    for i in range(m + 1):
        if ruiseki_b[i] <= k:
            best_b_num = i

    ans = 0
    j = best_b_num
    for i in range(n + 1):
        # a の最大の冊数まで調べる
        if ruiseki_a[i] > k:
            break

        # a の冊数 i に対する b の冊数 j
        # a が 1冊増えれば b が 1冊減る
        # 全ループの合計で高々 m 回
        while ruiseki_b[j] > k - ruiseki_a[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)


main()
