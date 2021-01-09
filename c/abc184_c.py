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

# 56m AC
r1, c1 = LI()
r2, c2 = LI()
if r1 == r2 and c1 == c2:
    print(0)
    exit()
if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
    exit()
if r1+c1 == r2+c2 or r1-c1 == r2-c2 or abs(r1-r2) + abs(c1-c2) <= 6:
    print(2)
    exit()
if (r1-c1) % 2 == (r2-c2) % 2:
    print(2)
    exit()
for i in range(1, 4):
    if (r1+i)+c1 == r2+c2 or (r1-i)+c1 == r2+c2 or r1+(c1+i) == r2+c2 or r1+(c1-i) == r2+c2\
            or (r1+i)-c1 == r2-c2 or (r1-i)-c1 == r2-c2 or r1-(c1+i) == r2-c2 or r1-(c1-i) == r2-c2:
        print(2)
        exit()

print(3)
