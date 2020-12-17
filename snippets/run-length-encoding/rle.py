def calc_rle_l(s: str) -> list:
    '''要素が [文字, 文字数] の リストをかえす'''
    now_c = s[0]
    cnt = 1
    res = []
    for i in range(1, len(s)):
        if now_c == s[i]:
            cnt += 1
        else:
            res.append([now_c, cnt])
            now_c = s[i]
            cnt = 1
    res.append([now_c, cnt])
    return res


print(calc_rle_l('BBBWW'))
