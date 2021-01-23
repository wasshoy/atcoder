n, t = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0
door_t = 0  # ドアが時刻door_tまで開いている
for ai in a:
    if door_t < ai:
        ans += t
    else:  # ドアが開いている間に人が来る
        ans += t - (door_t-ai)
    door_t = ai + t

print(ans)
