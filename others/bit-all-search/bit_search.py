# bit 全探索
# ２進数の桁が on / off 状態を表す
l = ['a', 'b', 'c']
n = len(l)
for i in range(2 ** n):
    bag = []
    for j in range(n):
        if i >> j & 1:  # 2進数表記の i の j 桁目が 1 のとき
            bag.append(l[j])
    print(bag)
