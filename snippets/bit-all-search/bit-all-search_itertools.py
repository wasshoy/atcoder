# itertools.product を使った簡潔なbit全探索
from itertools import product


l = ['a', 'b', 'c']
n = len(l)
for bag in product(l, repeat=n):
    print(bag)
