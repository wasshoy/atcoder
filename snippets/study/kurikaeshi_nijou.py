# Python の pow() でも実装されている繰り返し二乗法のアルゴリズムでべき乗の計算を O(log N) で行う
def pow(x, n):
    '''x^n を返す'''
    res = 1
    time = 0
    while n > 0:
        time += 1
        if n % 2 == 1:
            res *= x
        x *= x
        n >>= 1
    print(f'時間計算量 : {time}')
    return res


if __name__ == '__main__':
    print(pow(3, 8))
