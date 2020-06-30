# pythonは再帰呼び出しが余り早くない（らしい）
import time
import random
def merge(left, right):
    #print('merge {} {}'.format(left, right))
    merged = []
    left_i = 0
    right_i = 0

    while (left_i < len(left) and right_i < len(right)):
        if left[left_i] <= right[right_i]:
            merged.append(left[left_i])
            left_i += 1
        else:
            merged.append(right[right_i])
            right_i += 1
    
    if left_i < len(left):
        merged.extend(left[left_i:])
    if right_i < len(right):
        merged.extend(right[right_i:])
        
    #print('merged = {}'.format(merged))
    return merged

def merge_sort(l):
    #print('merge sort {}'.format(l))
    if len(l) <= 1:
        #print('return {}'.format(l))
        return l
    
    mid = len(l) // 2
    left_l = l[:mid]
    right_l = l[mid:]

    #print('left_l = {}'.format(left_l))
    left_l  = merge_sort(left_l)
    #print('right_l = {}'.format(right_l))
    right_l = merge_sort(right_l)

    return merge(left_l, right_l)

if __name__ == '__main__':
    #L = [5, 3, 6, 1, 2, 4, 0]
    N = 10 ** int(input())
    #print(N)
    L = [random.randint(1, N) for _ in range(N)]
    start = time.time()
    merge_sort(L)
    end = time.time()
    print('time: {}[s]'.format(end-start))