import sys
n, m = map(int, sys.stdin.readline().split())
n_hour = n % 12
n_deg = n_hour * 30 + 0.5 * m
m_deg = m * 6
# print(f'{n_deg=}, {m_deg=}')
ans = abs(n_deg - m_deg)
if ans >= 180: ans = 360 - ans
print(ans)