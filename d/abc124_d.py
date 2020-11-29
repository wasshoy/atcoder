import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def ST(): return input()
def SR(n): return [ST() for i in range(n)]
def LS(): return input().split()


INF = float('inf')

N, K = LI()
S = list(ST())

rle = []
curr = S[0]
cnt = 1
if curr == '0':
    rle.append(0)
for si in S[1:]:
    if si == curr:
        cnt += 1
    else:
        rle.append(cnt)
        curr = si
        cnt = 1
rle.append(cnt)
if S[-1] == '0':
    rle.append(0)
ans = sum(rle[:2*K+1])
curr_sum = ans
for i in range(0, len(rle)-2*K, 2):
    ans = max(ans, curr_sum)
    curr_sum += sum(rle[(i+2*K)+1:((i+2*K)+1)+2]) - sum(rle[i:i+2])
print(ans)
