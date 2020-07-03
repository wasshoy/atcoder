# 貪欲法 Greedy algorithm

その時点で最善の手を選び続けるアルゴリズム。
問題を部分的に分割し、それぞれの問題を独立して評価する。
DP と違うところは、「保持する状態は常に１つ」「一度選んだものは必ず答えに含まれる」点。
そのために、最適解を求められない場合がある。

## 例題

- https://atcoder.jp/contests/abc076/tasks/abc076_b
  - この問題は bit 全探索でも解ける

## 参考

- [Python で貪欲法(Greedy Algorithm)を実装してみる-ABC076](https://nashidos.hatenablog.com/entry/2019/12/30/154116)
