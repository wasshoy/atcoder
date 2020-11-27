# 挿入ソート
# 先頭の要素からはじめて、 1 ~ i 番目 要素の中でa[i]を適切な場所へ移動する
# O(n ^ 2)
def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        v = a[i]  # 挿入する要素
        print(f'挿入する要素：{a[i]=}')
        for j in reversed(range(i)):  # 後ろから見ていく
            print(f'{a[j]=} と {v=}')
            if a[j] > v:
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                break
        print(f'{a=}')
    return a


if __name__ == '__main__':
    l = [4, 2, 1, 3]
    print(l)
    print('▼')
    print(insert_sort(l))
