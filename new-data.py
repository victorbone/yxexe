import pandas as pd

# ---------------------------
# 步骤1：读取 Table01.csv（不使用文件中第一行作为列名），删除前38行数据（包括原文件的第一行列名）
# ---------------------------
df = pd.read_csv("Table01.csv", header=None)
# 删除前38行数据（包括原文件的第一行列名）
df_reduced = df.iloc[38:].reset_index(drop=True)

# ---------------------------
# 步骤2：删除剩余数据的前2列，并保存为 Table01_s.csv（不保留 header）
# ---------------------------
df_reduced = df_reduced.iloc[:, 2:]
df_reduced.to_csv("Table01_s.csv", header=False, index=False, encoding="utf-8-sig")
print("已生成 Table01_s.csv")

# ---------------------------
# 步骤3：读取 Table01_s.csv（无 header），对其进行转置，并保存为 Table01_transposed.csv
# ---------------------------
df_s = pd.read_csv("Table01_s.csv", header=None)
df_transposed = df_s.T
df_transposed.to_csv("Table01_transposed.csv", header=False, index=False, encoding="utf-8-sig")
print("已生成 Table01_transposed.csv")

# ---------------------------
# 步骤4：读取 Table01_transposed.csv，设置第一行为列名，
#         在最前面插入一列 "label"（所有值设为 0），保存为 ge01.csv
# ---------------------------
df_final = pd.read_csv("Table01_transposed.csv", header=0)
df_final.insert(0, "label", 0)
df_final.to_csv("D:/pyside6_code/demo03/ge_data/ge01.csv", index=False, encoding="utf-8-sig")
print("已生成 ge01.csv")
