n = int(input())
root = int(n**0.5)
is_prime = [True] * (n + 1)
is_prime[0] = False
is_prime[1] = False
for i in range(2, root+1):
    if not is_prime[i]:
        continue
    for j in range(2*i, n+1, i):
        is_prime[j] = False
ans = len([b for b in is_prime[:-1] if b])
print(ans)
