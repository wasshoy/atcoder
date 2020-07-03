# 再帰的な分割統治のアルゴリズム
# 適当な要素を一つを選び pivot とする
# pivotより左はpivot未満、右はpivot以上と並び替えて、分割してそれぞれを再帰的に解く
# 平均 O(n log n) : aの要素からなる順列は n! 通りあり、それぞれが当確率で出現するという仮定が成立する場合
# 最悪 O(n ^ 2) : pivot による 左右分割が極端に片方に偏った場合
# しかし、実用上は平均的に非常に高速であり、外部メモリを必要としない内部ソート であるという利点がある
# 内部ソート（外部メモリを必要としない）が、安定ソート（等しい値の場合元の順序を保つソート）ではない
def quick_sort(a, left, right):
    if right - left <= 1:  # 要素数が 1
        return
    pivot_index = (left + right) // 2  # 今回は pivot を中点としてみる
    pivot = a[pivot_index]
    a[pivot_index], a[right - 1] = a[right - 1], a[pivot_index]  # pivot と右端を入れ替える

    i = left  # ポインタ
    for j in range(left, right - 1):  # 配列を左から右へ全て見ていく
        if a[j] < pivot:  # pivot 未満の要素があれば a[i] と入れ替えて左に詰めていく
            a[i], a[j] = a[j], a[i]
            i += 1
    # 端まで来たら右端に置いておいた pivot を適切な位置へ挿入
    a[i], a[right - 1] = a[right - 1], a[i]

    quick_sort(a, left, i)  # pivot 未満の左
    quick_sort(a, i + 1, right)  # pivot 以上の右


l = [8, 2, 6, 9, 1, 4, 3, 5]
n = len(l)
quick_sort(l, 0, n)
print(l)


# クイックソートの乱択化
# 乱択アルゴリズム : ランダムに選ぶ という操作が含まれる アルゴリズム
# ランダム選択の利点 : 偏ったケースを避けることができる
