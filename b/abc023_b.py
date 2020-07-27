# ?m AC
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


n = I()
s = S()
base = 'b'
is_ok = False
if s == 'b':
    print(0)
    exit()
i = 1
while i <= 100:
    if i % 3 == 1:
        base = 'a' + base + 'c'
    elif i % 3 == 2:
        base = 'c' + base + 'a'
    else:
        base = 'b' + base + 'b'
    if base == s:
        is_ok = True
        break
    i += 1
if is_ok:
    print(i)
else:
    print(-1)
