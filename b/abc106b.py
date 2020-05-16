import math
import sys
n = int(sys.stdin.readline())
ans = 0
for i in range(3, n + 1, 2):
    # print(f'{i=}', end=' ')
    count = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            # print(f'{i} % {j} is 0.')
            count += 2
    if count == 8:
        # print(f'{i} have just 8 divisors.')
        ans += 1
print(ans)