# Python の処理における時間計算量

l, dict, set : 大きさ n の それぞれの collection 型オブジェクト
k : もうひとつの collection 型オブジェクト
b : 追加される collection 型オブジェクトの大きさ

## collection 型

参考

- https://qiita.com/bee2/items/4ab87d05cc03d53e19f9

## 共通

- 大きさ取得 len(a) : O(1)
- 要素へのアクセス a[i] : O(1)
- イテレーション for など : O(n)
  - ただし、要素を直接取り出す方インデックスを指定する早い

## list / tuple

- スライス l[i:j] : O(j - i)
- in 演算子 : O(n)
- 値の代入 l[i] = v : O(1)
- 値の代入 l[i:j] = lists : O(j - i)
- 値の追加
  - 末尾に追加 l.append(v) : O(1)
  - i 番目に追加 l.insert(v, i)
  - 末尾にリストを追加 l.extend(list)
- 値の削除
  - 末尾削除 l.pop() : O(1)
  - i 番目削除 l.delete(i) : O(n)
  - pop よりは スライス
  - delete O(k × n) よりは 再作成 O(n)

## dictionary

- in 演算子
  - キーに対して : O(1)
  - 値に対して : O(n)
  - (key, value) in dict.items() : O(1)
    - hash table の利用による速さ
- 値の代入 dict[i] = v : O(1)
- 値の追加
  - 要素を追加 dict[key] = v : O(1)
  - 辞書の結合 dict.update(dict2) : O(b)
- 値の削除 : dict.pop(k) : O(1)

## set

- in 演算子 : O(1)
- 値を追加 set.add(v) : O(1)
- 値の削除 set.discard(v) : O(1)

## その他操作の速度

### 逐次追加 vs 結合

- あんま差はなさそう

## 参考

- [Pythonista なら知らないと恥ずかしい計算量のはなし](https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb)
