# https://atcoder.jp/contests/abc150/tasks/abc150_c
import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

seq =(i for i in range(1,n+1))
l = list(itertools.permutations(seq))
print(abs(l.index(p)-l.index(q)))