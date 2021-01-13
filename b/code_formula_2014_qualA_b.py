a, b = map(int, input().split())
pa = list(map(int, input().split()))
pb = list(map(int, input().split()))
ans = ['x'] * 10
for i in pa:
    ans[i-1] = '.'
for i in pb:
    ans[i-1] = 'o'
ans = ans[::-1]
for start, end, i in [(0, 4, 0), (4, 7, 1), (7, 9, 2), (9, 10, 3)]:
    print(' ' * i + ' '.join(ans[start:end][::-1]))
