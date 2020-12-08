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

# 33
s = list(S())
if len(set(s)) == 1:
    print(0)
    exit()

ans = len(s)
for c in set(s):
    # c に統一するように優先的に操作する
    base = s[:]
    cnt = 0
    while True:
        res = ''
        for i in range(len(base)-1):
            if base[i] == c or base[i+1] == c:
                res += c
            else:
                res += base[i+1]
        cnt += 1
        if len(set(res)) == 1:
            break
        base = res
    ans = min(ans, cnt)
print(ans)
