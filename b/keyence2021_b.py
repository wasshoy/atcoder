# 55m + 3WA AC
from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
cter = Counter(a)
tpls = sorted(cter.items(), key=lambda x: x[0])
ans = 0
num_cnt = 0
for key, val in tpls:
    if key != num_cnt:
        break
    ans += min(k, val)
    k = min(k, val)
    num_cnt += 1
print(ans)
