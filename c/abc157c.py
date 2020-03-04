n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
ans = float('inf')
k = 0
if n == 2: k = 10
elif n == 3: k = 100
for i in reversed(range(k, 1000)):
    #print(f'i: {i}')
    flg = True
    for s, c in sc:
        #print(f'{s}桁目が{c}?', end=' ')
        if list(str(i))[s-1] == str(c): continue
        #print('No!')
        flg = False
    
    if flg:
        ans = min(ans, i)
        #print('ans: ', ans)
if ans == float('inf'): ans = -1
print(ans)