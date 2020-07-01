# 再帰を利用したソートアルゴリズム
# 分割した配列をソートし、それら同士をマージすることで並び替える
# 「分割」 と 「統治」 の処理に分けることができる
# O(n log n)
# 空間計算量は O(n)
# 内部ソート（外部メモリを必要としない）ではないが、安定ソート（等しい値の場合元の順序を保つソート）である
def merge_sort(a, left, right):
    print(f'{(left, right)=}')
    if right - left == 1:  # 要素数が 1
        print('要素が 1')
        return
    # 分割処理 O(log n)
    # 配列を左右に分割してそれぞれソート
    mid = (left + right) // 2
    print(f'左 : {(left, right, mid)=}')
    merge_sort(a, left, mid)
    print(f'右 : {(left, right, mid)=}')
    merge_sort(a, mid, right)

    # 統治処理 O(log n)
    # それぞれの初めの要素から大小を比較して、小さい方を最終結果の配列に入れていく
    # 右側を反転させて配列の末尾同士をくっつけた配列を利用する
    buf = [elem for elem in a[left:mid]]
    buf += [elem for elem in a[mid:right]]  # 末尾の要素から入れていく
    # マージ
    # 左側と右側のポインタ
    poi_left = 0
    poi_right = len(buf) - 1
    for i in range(left, right):  # O(n)
        # 左側の現在指し示されている要素の方が小さい
        if buf[poi_left] <= buf[poi_right]:
            a[i] = buf[poi_left]
            poi_left += 1
        # 右側の現在指し示されている要素の方が小さい
        else:
            a[i] = buf[poi_right]
            poi_right -= 1
    print(f'現在の{a=}')


l = [8, 2, 6, 9, 1, 4, 3, 5]
merge_sort(l, 0, len(l))
print(l)
