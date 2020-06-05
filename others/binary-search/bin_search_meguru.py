# めぐる式二分探索
# 方針
# left は常に条件を満たさない
# right は常に条件を満たす
# right - left = 1になるまで範囲を狭める(最終的にrightが貢献を満たすものの最小になる)

# 条件を満たすかどうか
def is_ok(l, i, key):
    if l[i] >= key:
        return True


def binary_seach(l, key):
    left = -1  # right = 0が条件を満たさない場合もあるので初期値は左端の外
    right = len(l)  # 右端が条件を満たさない場合もあるので初期値は右端の外

    # 汎用的な二分探索アルゴリズム
    while right - left > 1:
        mid = left + (right - left) // 2
        if is_ok(l, mid, key):
            right = mid
        else:
            left = mid

    return right


if __name__ == '__main__':
    a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]
    print(f'{binary_seach(a, 51)=}')
    print(f'{binary_seach(a, 1)=}')
    print(f'{binary_seach(a, 910)=}')
    print(f'{binary_seach(a, 52)=}')
    print(f'{binary_seach(a, 0)=}')
    print(f'{binary_seach(a, 911)=}')
