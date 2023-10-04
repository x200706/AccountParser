### 預期製作的新功能
- 例外處理顯示錯誤訊息，減少csv自行排查錯誤所花費的時間
  
***
### Require
- Python3
- Pandas2.1.1
```shell
pip install pandas==2.1.1
```
- A account `*.csv` file which is named `acc.csv`, format：
```
名稱, 日期, 收支, 分類, 金額
資產盤點, 20230921, I, 資產, 15000
眼科檢查, 20230925, O, 醫療保健, 100
雜貨店, 20230925, O, 飲食, 199
義麵館, 20230925, O, 飲食, 315
寶雅, 20230926, O, 衣物或衛生, 700
```
(`Space` after `comma` is necessary.)
>**PS：**
>
>'I' means 'input' and 'O' means 'output'.
