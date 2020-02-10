# https://atcoder.jp/contests/abc154/tasks/abc154_d
def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ex = [0 for _ in range(n)]
    for i in range(n):
        ex[i] = (p[i]+1)/2
    
    sumex = sum(ex[:k])
    tmp = sum(ex[:k])
    for i in range(n-k):
        tmp = tmp + (ex[i+k] - ex[i])
        sumex = max(sumex, tmp)
    print(sumex)
    
main()