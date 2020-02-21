# https://atcoder.jp/contests/abc117/tasks/abc117_c
def main():
    n, m = map(int, input().split())
    *x, = map(int, input().split())
    if n >= m: return 0
    x = sorted(x)
    sec_x = [abs(x[i] - x[i+1]) for i in range(m-1)]
    sec_x = sorted(sec_x)
    ans = sum(sec_x[:(m-1 - (n-1))])
    return ans

print(main())