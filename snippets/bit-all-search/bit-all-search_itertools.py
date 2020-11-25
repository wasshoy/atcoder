# itertools.product を使った簡潔なbit全探索
from itertools import product

# prduct(l1, l2, ...) : l1, l2, ... の直積集合を返す

foods = ['apple', 'banana', 'chocolate', 'donut', 'egg']
n = len(foods)
for bits in product((False, True), repeat=n):
    selected = [food for food, bit in zip(foods, bits) if bit]
    print(selected)
