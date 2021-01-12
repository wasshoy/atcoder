import sys
def input(): return sys.stdin.readline().strip()


INF = float('inf')
MOD = 10**9 + 7

# 12m AC
n, a, b = map(int, input().split())
s = [int(input()) for _ in range(n)]
s.sort()
if s[-1] - s[0] == 0:
    print(-1)
    exit()
p = b / (s[-1] - s[0])
q = (a*n - (b / (s[-1] - s[0]))*sum(s)) / n
print(p, q)
