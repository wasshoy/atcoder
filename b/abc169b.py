import sys
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())


n = I()
a = LI()
ans = a[0]
if 0 in a:
    print(0)
    sys.exit()
for ai in a[1:]:
    ans *= ai
    if ans > 10 ** 18:
        ans = -1
        break

print(ans)
