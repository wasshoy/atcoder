# 16m AC
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
curr = 0
p = 0
for i, elem in enumerate(a):
    curr += elem
    if curr >= s//2:
        p = i
        break
ans = min(abs(sum(a[:p]) - sum(a[p:])), abs(sum(a[:p+1]) - sum(a[p+1:])))
print(ans)
