import re
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


sd = S()
sd = sd.replace('?', '.')  # 正規表現を使うため、「任意の一文字」を表す「.」に変換しておく
t = S()

# s' の先頭から len(t) 文字を見て、 ? を 置き換えることで t にできる場合、
# t のために 使った s の ? 以外の ? を全て a に変えた文字列を候補の一つとする
ans = []
for i in range(len(sd) - len(t) + 1):
    if not re.match(sd[i:i + len(t)], t):
        continue
    kouho = (sd[:i] + t + sd[i + len(t):]).replace('.', 'a')
    ans.append(kouho)

if not ans:
    print('UNRESTORABLE')
    sys.exit()

print(min(ans))  # 文字列 の min は 辞書順の最小になる
