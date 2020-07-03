import sys
n, k = map(int, sys.stdin.readline().split())
*a, = map(int, sys.stdin.readline().split())
sorted_a = sorted(a, reverse=True)
good_taste = sorted_a[0]
for i in range(1, k):
    if sorted_a[i] < 0: continue
    good_taste += sorted_a[i]
print(good_taste)