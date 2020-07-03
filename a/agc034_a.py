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


n, a, b, c, d = LI()
a, b, c, d = a - 1, b - 1, c - 1, d - 1
s = S()

# 移動する部分に連続した岩がないか
for i in range(a + 1, max(c, d) - 1):
    if s[i:i + 2] == '##':
        print('No')
        sys.exit()

if c < d:
    print('Yes')
    sys.exit()

else:
    # どこかで a が b を追い越す必要がある
    # b がどこに居ても追い越せるための 3マス連続の空きマスがあるか
    for i in range(b, d + 1):
        if s[i - 1:i + 2] == '...':
            print('Yes')
            sys.exit()
    print('No')
