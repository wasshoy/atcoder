# 94m AC
s = input()
# xを除いて左と右からそれぞれ見る
s_ex = ''.join([c for c in s if c != 'x'])
if s_ex != s_ex[::-1]:
    print(-1)
    exit()
l = [i for i, c in enumerate(s) if c != 'x']
r = [i for i, c in enumerate(s[::-1]) if c != 'x']
cntl = 0
cntr = 0
ans = 0
for i, j in zip(l, r):
    if i+cntl < j+cntr:
        cntl, ans = cntl + j+cntr - (i+cntl), ans + j+cntr - (i+cntl)
    elif i+cntl > j+cntr:
        cntr, ans = cntr + i+cntl - (j+cntr), ans + i+cntl - (j+cntr)

first_x_cnt = 0
for c in s:
    if c == 'x':
        first_x_cnt += 1
    else:
        break
last_x_cnt = 0
for c in s[::-1]:
    if c == 'x':
        last_x_cnt += 1
    else:
        break
ans += abs(first_x_cnt - last_x_cnt)
ans //= 2
print(ans)
