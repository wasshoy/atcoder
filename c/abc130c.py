# https://atcoder.jp/contests/abc130/tasks/abc130_c
def main():
    W, H, x, y = map(int, input().split())
    # (x, y)と中心を通る直線で分割すると必ず半分の面積になる（最大値）
    ans = W * H / 2
    # (x, y)が中心だった場合どんな直線でも必ず半分になる
    num = 1 if (2*x == W and 2*y == H) else 0
    print(ans, num)
if __name__ == '__main__':
    main()
