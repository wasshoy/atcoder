# オーダーの見積もり目安(一般的なアルゴリズムと Python での実装を混同しているので注意)

## 重要

- Python の list は可変長配列というデータ構造

## 1

- 配列の要素へのアクセス
- Python のリストの末尾に要素追加・削除(l.append(v), l.pop())
- 単方向連結リストの要素の挿入・削除
- deque の両端の要素の追加・削除
- 連想配列(Python の dict)の要素の検索・挿入・削除
- Python のリストの長さ取得
- 優先度付きキューの最小値の取得

## log N

- 優先度付きキューの要素の追加/削除

## N

- 配列の要素の挿入・削除
- Python のリストの i 番目削除(l.pop(i))・要素 v の削除(l.remove(v))
  - 削除した後、インデックスを振り直す必要があるから遅い
- 値 v の検索(Python の v in l)
- 単方向連結リストの要素へのアクセス
- 長さ N の文字列(配列)を逆順にソート
- Python のリストのヒープ化(heapq.heapify(l))

## N log N

- 配列のソート(Python の l.sort())
- 値 v の検索(ソート済み配列):二分探索という

## 参考

- []()
- [Python で"in list"から"in set"に変えただけで爆速になった件とその理由](https://qiita.com/kitadakyou/items/6f877edd263f097e78f4)
