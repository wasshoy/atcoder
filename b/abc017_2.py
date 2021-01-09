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

# 12m AC
x = S()
is_choku = True
n = len(x)

i = 0
while i < n:
    if i < n and x[i:i+2] == 'ch':
        i += 2
        continue
    elif x[i] == 'o' or x[i] == 'k' or x[i] == 'u':
        i += 1
        continue
    else:
        is_choku = False
        break
ans = 'YES' if is_choku else 'NO'
print(ans)
