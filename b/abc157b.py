a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
mark = [[False, False, False] for _ in range(3)]

for i in range(3):
    for j in range(3):
        if a[i][j] in b:mark[i][j] = True
ans = 'No'
for i in range(3):
    if all(mark[i]):
        ans = 'Yes'
        break
        
for j in range(3):
    if mark[0][j] and mark[1][j] and mark[2][j]:
        ans = 'Yes'
        break
        
if (mark[0][0] and mark[1][1] and mark[2][2]) or (mark[0][2] and mark[1][1] and mark[2][0]): ans = 'Yes'
print(ans)