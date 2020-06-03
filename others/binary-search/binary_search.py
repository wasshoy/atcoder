# 二分探索

import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


# 配列 l に 値vが含まれるかどうかを判定する
# O(log n)
def is_bin_search(l, v):
    left = 0  # 探索範囲の左端
    right = len(l) - 1  # 探索範囲の右端
    mid = (left + right) // 2
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == v:
            return True
        elif v < l[mid]:
            right = mid - 1  # 真ん中の左隣
        else:
            left = mid + 1  # 真ん中の右隣
        mid = (left + right) // 2
    return False
