#やりたいこと
1. アイテムの金銭効率検索、比較を簡単にできるサービス
1. パッチverup時に金銭効率は自動更新する

#できればやりたいこと
1. 条件を与えると最高効率のビルドパスを提案してくれる機能
2. ユーザーによるビルドガイド登録+システムでの効率自動計算で、ビルド考えるのめんどくさい勢も簡単に最適なビルドを選択可能

**​
以下はまず最低ラインをベースに考える**

##表示したい項目の整理
- アイコン+アイテム名
- 合計の金銭価値
- 金額
- 金銭効率
- ステータスと金銭価値のリスト
- 追加効果と金銭価値のリスト(評価不可能なものは色付け)
- 素材
- 合成先

## つけたい機能
- 検索
  - アイテム名
  - 種類とかの公式でもできるアレ
- ソート
- 複数のビルド（アイテム群）を並べて比較

##備考
- サモリフ限定で良い
- 状況で金銭価値が変わるアイテムは○〜○とか、○+といった形で表現したい
- アイテムティアは自動ソート(下がティア高いやつ)
- どのステータス/効果を評価しているのか一目で分かる

##db設計メモ
- パッチバージョンは外だしして外部キー参照
- 金銭能率マスタ外だし(金銭効率ベース変動の可能性があるため)
- タグマスタ外だし(変動の可能性があるため)
- マップマスタはなし、jsonの解析時にサモリフで絞ってレコード登録する
- アイテム相関テーブルはなし。アイテムモデル内のフィールドで対応する(カンマ区切りinteger)

​
##追加効果の金銭価値換算パターン
- スタック数に依存するステータス増加(グインソー、ROA)
  - スタック数が分かれば評価可能
- 自身のステータスに依存するステータス増加(帽子)
  - ステータスが分かれば評価可能
  - 評価は最後に行う必要がある点に注意
- 相手のステータスに依存する(LW)
  - 評価不可能
- アクティブ
  - 評価不可能
- 状況限定なステータス増加(jgタリスマン、スペクターカウル)
  - 状況が分かれば評価可能
