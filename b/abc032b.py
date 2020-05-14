import sys
s = sys.stdin.readline()
k = int(sys.stdin.readline())
sets = set()
for i in range(len(s) - k):
    if s[i:i + k] in sets: continue
    sets.add(s[i:i + k])
    # print(f'{i=}, {i+k=}')
    # print(s[i:i + k])
print(len(sets))