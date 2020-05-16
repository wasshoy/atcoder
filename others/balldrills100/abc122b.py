import sys
s = sys.stdin.readline()
ans = 0
for i in range(len(s)):
    # print(f'{s[i]=}')
    if s[i] not in {'A', 'C', 'G', 'T'}: continue
    length = 1
    for j in range(i + 1, len(s)):
        if s[j] in {'A', 'C', 'G', 'T'}:
            # print(f'{s[j]=}')
            length += 1
        else: break
    ans = max(ans, length)
    # print(f'{ans=}')
print(ans)