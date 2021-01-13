# 13m AC
n, a, b = map(int, input().split())
s = input()
i = 0
rank_b = 0
for c in s:
    if c == 'b':
        rank_b += 1
        if rank_b <= b and i < a+b:
            print('Yes')
            i += 1
        else:
            print('No')
    elif c == 'a':
        if i < a+b:
            print('Yes')
            i += 1
        else:
            print('No')
    else:
        print('No')
