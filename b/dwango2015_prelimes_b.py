# 32m AC
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


s = S()
n = len(s)
ans = 0
nico_cnt = []
cnt = 0
i = 0
is_nico = False
while i < n:
    # print(f'{(i, s[i])=}')
    if s[i] == '2':
        if i > 0 and s[i - 1] == '2':
            # is_nico = False
            if cnt > 0:
                nico_cnt.append(cnt)
                cnt = 0
        is_nico = True
    elif is_nico and s[i] == '5':
        cnt += 1
        is_nico = False
    else:
        is_nico = False
        if cnt > 0:
            nico_cnt.append(cnt)
            cnt = 0
    i += 1
    # print(f'{cnt=}')
    # print(nico_cnt)
if cnt > 0:
    nico_cnt.append(cnt)
# print(nico_cnt)
for m in nico_cnt:
    ans += m * (m + 1) // 2
print(ans)
