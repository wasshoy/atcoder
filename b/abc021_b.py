import sys
def input(): return sys.stdin.readline().strip()


# 7m AC
n = int(input())
a, b = map(int, input().split())
k = int(input())
*p, = map(int, input().split())

if a in p or b in p:
    print('NO')
elif len(p) != len(set(p)):
    print('NO')
else:
    print('YES')
