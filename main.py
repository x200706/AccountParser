import pandas as pd
import os

def check():
  pwd = os.getenv("MIMA")
  user_input_pwd = input('使用本程式前，先核對身分：')
  if user_input_pwd != pwd:
    print('你不是本人...請回吧> <|||')
    exit()

check()

# 載入記帳
file_path = 'acc.csv'
df = pd.read_csv(file_path)
df.columns = df.columns.str.replace(' ', '')  # trim

# 顯示記帳
print(df)

# ---------------情報區 --------------- #
df['金額'] = pd.to_numeric(df['金額']) # 字串轉貨幣

# 計算總收入
total_income = df[df['收支'] == ' I']['金額'].sum()
print('總收入：', total_income)

# 計算總支出
total_expense = df[df['收支'] == ' O']['金額'].sum()
print('總支出：', total_expense)

# 計算總資產
print('總資產：', total_income - total_expense)
