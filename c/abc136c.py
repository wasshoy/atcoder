# https://atcoder.jp/contests/abc136/tasks/abc136_c
def main():
    n = int(input())
    h = list(map(int, input().split()))

    ans = 'Yes'
    # 右から見ていく
    for i in reversed(range(1,n)):
        if h[i-1] <= h[i]: continue
        # 左隣が1だけ大きい場合1減らして続ける
        if h[i-1]-1 == h[i]:
          h[i-1] = h[i-1] - 1
          continue
        # 左隣が2以上大きい場合
        ans = 'No'
        break
    print(ans)
    
if __name__ == '__main__':
    main()
