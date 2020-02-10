# https://atcoder.jp/contests/abc154/tasks/abc154_c
# coding: utf-8
# Your code here!
def main():
    n = int(input())
    a = list(map(int, input().split()))
    seta = set(a)
    ans = 'YES' if len(a) == len(seta) else 'NO'
    print(ans)
        
main()