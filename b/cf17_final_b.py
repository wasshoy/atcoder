from collections import Counter
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


s = list(S())
c = Counter(s)

a = c.get("a", 0)
b = c.get("b", 0)
c = c.get("c", 0)

if max(a, b, c) - min(a, b, c) >= 2:
    print("NO")
else:
    print("YES")
