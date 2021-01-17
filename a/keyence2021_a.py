# 18m + 1WA AC
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ma = a[0]
mb = b[0]
ans = [a[0]*b[0]]
for ai, bi in zip(a[1:], b[1:]):
    ma = max(ma, ai)
    ans.append(max(ma*bi, ans[-1]))
print(*ans, sep='\n')
