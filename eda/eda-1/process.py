import pandas as pd

# データを読み込む
df = pd.read_csv('../../baseline/train.csv')

# 全てのカラムのデータ型のみをリストとして抽出
column_types = [str(dtype) for dtype in df.dtypes]

# data_definition.csvを1行スキップして読み込み
data_definitions = pd.read_csv('data_definition.csv', skiprows=1, header=None)

# データ型リストをDataFrameとして作成
types_df = pd.DataFrame(column_types)

# data_definition.csvとデータ型情報を結合
result = pd.concat([data_definitions, types_df], axis=1)

# 結合結果を新しいCSVファイルに保存
result.to_csv('merged_data_definition.csv', index=False, header=False)