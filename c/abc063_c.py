n = int(input())
s = [int(input()) for _ in range(n)]
max_score = sum(s)
if max_score % 10 == 0:
    s = sorted(s)
    i = 0
    while i < n:
        now_score = max_score - s[i]
        if now_score % 10 != 0:
            max_score -= s[i]
            break
        i += 1
    if i == n:
        max_score = 0
print(max_score)
