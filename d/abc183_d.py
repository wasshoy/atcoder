import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


def calc_cumsum(l):
    cumsum = [0]
    for i in l:
        cumsum.append(cumsum[-1] + i)
    return cumsum


def imos(a, query):
    n = len(a)
    q = len(query)
    # 1. 加算処理 : 区間[l, r] に +v => a[l]に + v, a[r + 1]に - v
    for l, r, v in query:
        a[l] += v
        if r + 1 < n:
            a[r + 1] -= v
    # 2. 累積和計算 : 加算処理を行った配列の累積和を計算 => 各要素の値がクエリを行った最終結果になる(すごい)
    cumsum = calc_cumsum(a)[1:]
    return cumsum


n, w = LI()
query = LIR(n)
need = [0] * (2*10**5 + 10)
for i in range(n):
    query[i][1] -= 1
res = imos(need, query)
for need_yu in res:
    if need_yu > w:
        print('No')
        exit()
print('Yes')
