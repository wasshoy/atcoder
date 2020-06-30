# 先頭の要素からはじめて、 1 ~ i 番目 要素の中でa[i]を適切な場所へ移動する
# O(n ^ 2)
def insert_sort(a):
    n = len(a)
    for i in range(1, n):
        v = a[i]  # 挿入する要素
        for j in reversed(range(i)):  # 後ろから見ていく
            if a[j] > v:
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                break
    return a


l = [8, 2, 6, 9, 1, 4, 3, 5]
print(insert_sort(l))
