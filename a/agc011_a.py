# 27m AC
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


n, c, k = LI()
t = IR(n)
t.sort()
t_limit = list(map(lambda x: x+k, t))
ans = 0
i = 0
bus = 0
limit = 0
while i < n:
    # print(f'{(i, bus, limit, ans)=}')
    if bus == 0:
        # print('新しいバス')
        limit = t_limit[i]
        bus += 1
    elif bus < c:  # バスに空きがある
        # print('バスに空きがある')
        # print(f'{(i, t[i])=}')
        if t[i] <= limit:  # 間に合う
            # print('間に合う')
            bus += 1
        else:  # 新しいバスに乗る
            # print('間に合わない')
            ans += 1
            bus = 1
            limit = t_limit[i]
    else:  # バスが満杯
        ans += 1
        bus = 1
        limit = t_limit[i]
    i += 1
print(ans + 1)
