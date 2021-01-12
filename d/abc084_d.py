# 18m AC
# 10^5以下の素数を求める
n = 10 ** 5
root = int(n ** 0.5)
is_prime = [True] * (n+1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, root+1):
    if not is_prime[i]:
        continue
    for j in range(2*i, n+1, i):
        is_prime[j] = False

# 10^5以下の2017に似た数の個数の累積和を求める
cumsum = [0]
for i in range(1, n+1):
    if i % 2 != 0 and is_prime[i] and is_prime[(i+1)//2]:
        cumsum.append(cumsum[-1] + 1)
    else:
        cumsum.append(cumsum[-1])

ans = []
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    res = cumsum[r] - cumsum[l-1]
    ans.append(res)
print(*ans, sep='\n')
