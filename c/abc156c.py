n = int(input())
*x, = map(int, input().split())
x.sort()
ans = float('inf')

for i in range(x[0], x[n-1]+1):
    tmp = 0
    for j in x:
        tmp += (j - i)*(j - i)
    ans = min(ans, tmp)
print(ans)
