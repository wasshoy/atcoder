n, l = map(int, input().split())
tastes = [i + l for i in range(n)]
abs_tastes = [abs(taste) for taste in tastes]
ind = abs_tastes.index(sorted(abs_tastes)[0])
print(sum(tastes) - tastes[ind])
