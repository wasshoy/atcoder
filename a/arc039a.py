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


a, b = LS()
ans = int(a) - int(b)
b = int(b)
ans = max(ans, int('9' + a[1:]) - b)
ans = max(ans, int(a[0] + '9' + a[2]) - b)
ans = max(ans, int(a[:2] + '9') - b)
b = str(b)
a = int(a)
ans = max(ans, a - int('1' + b[1:]))
ans = max(ans, a - int(b[0] + '0' + b[2]))
ans = max(ans, a - int(b[:2] + '0'))
print(ans)
