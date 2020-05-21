import sys


def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]


a, b, k, l = LI()
ans = 0
if k >= l:
    if b * (k // l) + a * (k % l) <= b * (k // l + 1):
        ans += b * (k // l) + a * (k % l)
    else:
        ans += b * (k // l + 1)
else:
    if b <= a * k:
        ans += b
    else:
        ans += a * k
print(ans)
