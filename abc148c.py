# https://atcoder.jp/contests/abc148/tasks/abc148_c
from  fractions import gcd
a, b = map(int, input().split())

lcm = (a * b) // gcd(a, b)

print(lcm)