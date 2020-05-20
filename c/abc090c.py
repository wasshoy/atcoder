n, m = map(int, input().split())
if n < 2 and m < 2:
    ans = 1
elif n < 2:
    ans = m - 2
elif m < 2:
    ans = n - 2
else:
    ans = n * m - (2 * n + 2 * m - 4)
print(ans)
