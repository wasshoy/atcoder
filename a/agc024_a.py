a, b, c, k = map(int, input().split())
ans = a-b if k % 2 == 0 else b-a
if abs(ans) > 10**18:
    print('Unfair')
else:
    print(ans)
