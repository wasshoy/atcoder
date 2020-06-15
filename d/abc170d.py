
def I(): return int(input())
def LI(): return list(map(int, input().split()))


n = I()
a = LI()
cnt = [0] * ((10 ** 6) + 1)
for elem in a:
    cnt[elem] += 1

unique = []

for i in range((10 ** 6) + 1):
    if cnt[i] == 1:
        unique.append(i)

cnt = [0] * ((10 ** 6) + 1)

a = list(set(a))

for elem in a:
    for m in range(elem * 2, (10 ** 6) + 1, elem):
        cnt[m] = 1

ans = 0

for elem in unique:
    if cnt[elem] == 0:
        ans += 1

print(ans)
