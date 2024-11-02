メモ
## ランダムフォレストで目的変数をもとに特徴量の重要度分析をして抽出されたカラム一覧

- `lat`: 緯度（世界測地系）
- `nl`: 緯度（日本測地系、ミリ秒形式）
- `building_structure`: 建物構造（1:木造, 2:ブロック, 3:鉄骨造, 4:RC, 5:SRC, 6:PC, 7:HPC, 9:その他, 10:軽量鉄骨, 11:ALC, 12:鉄筋ブロック, 13:CFT）
- `floor_count`: 建物階数（地上）
- `year_built`: 築年月（建築年月 yyyymm）
- `land_youto`: 用途地域（1:第一種低層住居専用, 2:第二種中高層住居専用, 3:第二種住居, 4:近隣商業, 5:商業, 6:準工業, 7:工業, 8:工業専用, 10:第二種低層住居専用, 11:第一種中高層住居専用, 12:第一種住居, 13:準住居, 14:田園住居地域, 99:無指定）
- `land_kenpei`: 建ぺい率（単位: %）
- `land_youseki`: 容積率（単位: %）
- `dwelling_unit_window_angle`: 主要採光面
- `unit_area`: 専有面積
- `post1`: 郵便番号（上位3桁）
- `addr1_2`: 市区郡町村
- `walk_distance2`: 徒歩距離2（駅またはバス停からの距離、単位: m）
- `house_area`: 建物面積/専有面積（代表、単位: 平米）
- `snapshot_window_angle`: 向き（1:北, 2:北東, 3:東, 4:南東, 5:南, 6:南西, 7:西, 8:北西）
- `money_kyoueki`: 共益費/管理費（代表、単位: 円）
- `money_sonota1`: その他費用1（単位: 円）
- `parking_money`: 駐車場料金（代表、単位: 円）
- `parking_distance`: 駐車場距離（単位: m）
- `convenience_distance`: コンビニ距離（単位: m）
- `super_distance`: スーパー距離（単位: m）
