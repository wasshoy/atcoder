
n = input()
if int(n[-1]) in {0, 1, 6, 8}:
    ans = 'pon'
elif int(n[-1]) == 3:
    ans = 'bon'
else:
    ans = 'hon'
print(ans)