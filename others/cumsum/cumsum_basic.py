def calc_cumsum(l):
    cumsum = [l[0]]
    for i in l[1:]:
        cumsum.append(cumsum[-1] + i)
    return cumsum


if __name__ == '__main__':
    l = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(f'元の配列 : {l}')
    ruiseki = calc_cumsum(l)
    print(f'累積和 :   {ruiseki}')
    print(f'l[4]から l[7]の和 (区間 [4, 8) の和) : {ruiseki[8] - ruiseki[4]=}')
