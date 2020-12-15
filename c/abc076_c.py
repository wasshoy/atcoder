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

s = S()
t = S()
res = ''
for i in range(len(s)-len(t)+1)[::-1]:  # 末尾から一致させれば最初の候補が辞書順最小になる
    cnt = 0
    for j in range(len(t)):
        if s[i+j] == t[j] or s[i+j] == '?':
            cnt += 1
    if cnt == len(t):
        print((s[:i] + t + s[i+len(t):]).replace('?', 'a'))
        break
else:
    print('UNRESTORABLE')
