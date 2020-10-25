n, l = map(int, input().split())
amidakuji = [input() for _ in range(l)]
atari = input()
position = atari.index('o')
# アタリの位置から開始地点の位置を辿る
for i in reversed(range(l)):  # あみだを下から辿る
    for direction in [-1, 1]:
        if 0 <= position + direction < 2*n - 1:
            if amidakuji[i][position + direction] == "-":  # 横線があればその方向にあみだを進める
                position += 2 * direction
                break
print(position//2 + 1)
