import math

a, b, h, m = map(int, input().split())
a_deg = h * 30 + m * 0.5
b_deg = m * 6
deg = abs(a_deg - b_deg) if abs(a_deg - b_deg) <= 180 else 360 - abs(a_deg - b_deg)
# print(f'{deg=}')
dis_sqrt = a**2 + b**2 - 2 * a * b * math.cos(math.radians(deg))
ans = math.sqrt(dis_sqrt)
# print(ans)

# 極座標を計算して２点のeuclid距離
a_th = math.radians(a_deg)
b_th = math.radians(b_deg)
a_x, a_y = a * math.cos(a_th), a * math.sin(a_th)
b_x, b_y = b * math.cos(b_th), b * math.sin(b_th)
dis = math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2)
print(dis)