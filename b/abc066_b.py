import sys
def input(): return sys.stdin.readline().strip()


# 14m AC
s = input()
n = len(s)
ans = 0
for i in range(n//2):
    if s[:i+1] == s[i+1:2*(i+1)] and 2*len(s[:i+1]) < n:
        ans = max(ans, 2*len(s[:i+1]))
print(ans)
