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
s = S()
ruiseki_e = [0] * n
ruiseki_w = [0] * n
if s[0] == 'E':
    ruiseki_e[0] += 1
else:
    ruiseki_w[0] += 1
for i in range(1, n):
    if s[i] == 'E':
        ruiseki_e[i] = ruiseki_e[i - 1] + 1
        ruiseki_w[i] = ruiseki_w[i - 1]
    else:
        ruiseki_w[i] = ruiseki_w[i - 1] + 1
        ruiseki_e[i] = ruiseki_e[i - 1]
ans = ruiseki_e[-1] - ruiseki_e[1]  # 一番左端をリーダーにした時
for i in range(1, n):
    ans = min(ans,
              ruiseki_w[i - 1] + (ruiseki_e[-1] - ruiseki_e[i]))
print(ans)
