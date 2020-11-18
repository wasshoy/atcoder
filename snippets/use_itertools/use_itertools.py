# itertools を使った順列  組み合わせ 直積 の生成
from scipy.special import comb
import itertools
from itertools import combinations_with_replacement


a = ['a', 'b', 'c', 'd']

# 順列(permutation)

# a から全て選ぶ n ! 通りの順列を生成
perm = list(itertools.permutations(a))
print(f'順列 nPn = n!, {len(perm)} 通り')
print(perm)

# a から r 個だけ選ぶ nPr 通りの順列を生成
r = 3
perm_3 = list(itertools.permutations(a, r))
print(f'順列 nP{r}, {len(perm_3)} 通り')
print(perm_3)

# 組み合わせ(combination)
# （ 順列の並び順を無視したものが組み合わせ ）
# a から r 個だけ選ぶ nCr 通りの組み合わせを生成
r = 3
combi = list(itertools.combinations(a, r))
print(f'組み合わせ {len(a)}C{r}, {len(combi)} 通り')
print(combi)

# 組み合わせの総数
print('5C3 (組み合わせの総数):', comb(5, 3, exact=True))  # 5個から 3個を選ぶ場合の数

# 直積(product)
# 集合 A と集合 B のそれぞれの要素を一つずつ取り出す組み合わせ
A = ('a', 'b', 'c')
B = ('d', 'e',)
C = ('f',)
prod_a_b = list(itertools.product(A, B))
prod_a_b_c = list(itertools.product(A, B, C))
print(f'{A}と{B}の直積')
print(f'{prod_a_b}')
print(f'{A}と{B}と{C}の直積')
print(prod_a_b_c)
# n 個の A の直積
n = 3
prod_a_n = list(itertools.product(A, repeat=n))
print(f'{n} 個の{A}の直積')
print(prod_a_n)

# 重複が許された組み合わせ
combi_dup = list(itertools.combinations_with_replacement(A, 3))
print(f'重複を許した{A}から3つ選ぶ組み合わせ')
print(combi_dup)
