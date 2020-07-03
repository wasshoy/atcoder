def main():
    N, W = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    w = [wv[i][0] for i in range(N)]
    v = [wv[i][1] for i in range(N)]
    vdp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(N):
        for weight in range(W+1):
            # 品物iを（選べるなら）選ぶ
            if weight >= w[i]:
                vdp[i+1][weight] = max(vdp[i][weight - w[i]] + v[i],
                                       vdp[i][weight])
            # 品物iを選ばない
            vdp[i+1][weight] = max(vdp[i+1][weight], vdp[i][weight])
    print(vdp[N][W])


if __name__ == '__main__':
    main()
