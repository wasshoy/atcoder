from collections import defaultdict


n, m = map(int, input().split())
*h, = map(int, input().split())
d = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)

ans = 0
for i in range(n):
    is_good = True
    for lighthouse in d[i]:
        if h[i] > h[lighthouse]:
            continue
        is_good = False
        break

    if is_good:
        ans += 1

print(ans)