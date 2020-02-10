# https://atcoder.jp/contests/abc126/tasks/abc126_c
import math

def calc_omote(x, y):
    score = x
    omo = 0
    while(score < y):
        score *= 2
        omo += 1
    return omo
        

n, k = map(int, input().split())
ans = 0
for i in range(1,n+1):
    omote = calc_omote(i, k)
    p = 1/(2**omote)
    ans += p/n
#sump /= n
print(ans)