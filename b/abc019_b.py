s = input()
ans = ''
cnt = 1
now_c = s[0]
for i in range(1, len(s)):
    if s[i] == now_c:
        cnt += 1
    else:
        ans += now_c + str(cnt)
        cnt = 1
        now_c = s[i]
ans += now_c + str(cnt)
print(ans)
