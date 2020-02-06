# https://atcoder.jp/contests/abc135/tasks/abc135_c
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        # 勇者iがまだi+1番目のモンスターを倒せる場合
        if b[i] > a[i]:
            # 残りの倒せる体数かi+1番目のモンスター全部
            ans += min(b[i] - a[i], a[i+1])
            # 残りのモンスターの数 か 全部倒されてたら0
            a[i+1] = max(a[i+1] - (b[i] - a[i]), 0)

    print(ans)

if __name__ == '__main__':
    main()