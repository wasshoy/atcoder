s = input()
k = int(input())
lengh = 0
ans = '1'
flag = True
for i in list(s):
    if i != '1':
        ans = i
        break
if k <= len(s):
    for i in list(s)[:k]:
        if i == '1': continue
        flag = False
        break
    if flag: ans = s[k-1]
print(ans)