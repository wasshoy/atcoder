from decimal import Decimal
import math

a, b = map(Decimal, input().split())
print(math.floor(a * b))
