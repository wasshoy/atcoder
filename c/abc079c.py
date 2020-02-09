# https://atcoder.jp/contests/abc079/tasks/abc079_c
def test():
    nums = list(map(int, list(input())))
    end = False
    for i in range(2 ** 3):
        ans = nums[0]
        res = '{}'.format(nums[0])
        for j in range(3):
            if (i >> j) & 1:
                ans += nums[j+1]
                res += '+{}'.format(nums[j+1])
            else:
                ans -= nums[j+1]
                res += '-{}'.format(nums[j+1])
        if ans == 7:
            end = True
            break
    print('{}=7'.format(res))

if __name__ == '__main__':
    test()
