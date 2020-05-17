import math

a, b, h, m = map(int, input().split())
a_deg = h * 30 + m * 0.5
b_deg = m * 6
deg = abs(a_deg - b_deg) if abs(a_deg - b_deg) <= 180 else 360 - abs(a_deg - b_deg)
# print(f'{deg=}')
dis_sqrt = a**2 + b**2 - 2 * a * b * math.cos(math.radians(deg))
ans = math.sqrt(dis_sqrt)
print(ans)