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
MOD = 10**9 + 7

# can't solved
n = I()
a = LI()
is_ok = True
ball = [0] * (n+1)
for i in reversed(range(1, n+1)):
    cnt = sum([ball[j] for j in range(i, n+1, i)])
    if cnt % 2 == a[i-1]:
        continue
    else:
        ball[i] = 1
        cnt += 1
        if cnt <= n and cnt % 2 == a[i-1]:
            continue
        else:
            is_ok = False
            break
if is_ok:
    ans = [i for i in range(n+1) if ball[i] == 1]
    print(len(ans))
    if ans:
        print(*ans, sep='\n')
else:
    print(-1)
