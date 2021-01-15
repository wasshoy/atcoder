n = int(input())
a = list(map(int, input().split()))
ans = 0
for ai in a:
    if ai % 2 == 0:
        while ai % 2 == 0:
            ans += 1
            ai //= 2
print(ans)
