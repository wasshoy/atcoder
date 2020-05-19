import fractions
def count(n, m, l):
    c_m = n // m
    c_l = n // l
    c_ml = n // (m * l // fractions.gcd(m, l))
    return n - (c_m + c_l - c_ml)

a, b, c, d = map(int, input().split())
b_tar = count(b, c, d)
a_tar = count(a, c, d)
is_plus_a = not(bool(a % c == 0 or a % d == 0))
ans = b_tar - a_tar
if is_plus_a: ans += 1
print(ans)