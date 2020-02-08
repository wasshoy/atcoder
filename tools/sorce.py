def test(input):
    lines = input.read().split('\n')
    # リストであるlinesに一行ごとの入力が格納されている
    # https://atcoder.jp/contests/abc153/tasks/abc153_a
    H, A = map(int, lines[0].split())
    ans = H // A if H % A == 0 else H // A + 1
    return ans