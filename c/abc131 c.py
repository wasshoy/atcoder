# https://atcoder.jp/contests/abc131/tasks/abc131_c
import fractions

def main():
    a, b, c, d = map(int, input().split())
    # (bまでの条件を満たす数の個数) - (a-1までの条件を満たす数の個数)
    l =  (c * d) // fractions.gcd(c, d)
    # 条件: b,cどちらでも割り切れないもの = 全体 - bかcで割り切れるもの
    cntb = b - ((b // c) + (b // d) - (b // l))
    cnta = (a-1) - (((a-1) // c) + ((a-1) // d) - ((a-1) // l))
    ans = cntb - cnta

    print(ans)

if __name__ == '__main__':
    main()
