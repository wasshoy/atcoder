s = input()
ans = ''
for c in s:
    if c in {'0', '1'}:
        ans += c
    if c == 'B':
        if len(ans) != 0:
            ans = ans[:-1]
print(ans)