def main():
    n, k = map(int, input().split())
    *a, = map(int, input().split())
    ans = 1
    n -= k
    while n > 0:
        ans += 1
        n -= k - 1
    return ans

print(main())