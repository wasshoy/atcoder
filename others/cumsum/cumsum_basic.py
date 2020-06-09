def calc_cumsum(l):
    cumsum = [l[0]]
    for i in l[1:]:
        cumsum.append(cumsum[-1] + i)
    return cumsum


print(calc_cumsum([1, 1, 2, 3, 5, 8, 13, 21, 34]))
