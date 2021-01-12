import sys
def input(): return sys.stdin.readline().strip()


# not AC(4WA + 解説)
x, y = map(int, input().split())
ans = 0
ai = x
while ai <= y:
    ans += 1
    ai *= 2
print(ans)
