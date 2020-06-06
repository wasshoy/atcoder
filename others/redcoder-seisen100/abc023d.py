import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


n = I()
h = []
s = []
for _ in range(n):
    hi, si = LI()
    h.append(hi)
    s.append(si)


def is_ok(t, i):
    if t >= i:
        return True
    return False


left = -1
right = 10 ** 9 + n * 10 ** 9 + 1
# O(log right)
while right - left > 1:
    middle = (left + right) // 2
    # 高さmiddle以内に割ることができる秒数の小さい順に並び替える
    # O(n log n)
    limit_t = sorted([(middle - hi) // si for hi, si in zip(h, s)])
    if all([is_ok(time, i) for i, time in enumerate(limit_t)]):
        right = middle
    else:
        left = middle
print(right)
