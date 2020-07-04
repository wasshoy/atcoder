# 配列の中で大小が逆転している隣同士の要素を入れ替える
# O(n ** 2)
# O(n ^ 2)
def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in reversed(range(i + 1, n)):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


l = [4, 5, 1, 3, 7, 9, 0, 2, 8]
print(bubble_sort(l))
