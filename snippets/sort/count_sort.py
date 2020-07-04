# 日本語：計数ソート
# O(n)でできることがある
# これの発展が基数ソート
def count_sort(arr):
    max_n = max(arr)
    min_n = min(arr)
    count = [0 for _ in range(max_n - min_n + 1)]
    for ele in arr:
        # 値ごとの出現回数
        count[ele - min_n] += 1
    sort_arr = [ele for ele, cnt in enumerate(count, start=min_n) for _ in range(cnt)]
    return sort_arr

if __name__ == '__main__':
    l = [4, 5, 1, 2, 19, 12, 32]
    print(*count_sort(l))