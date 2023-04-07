# Backtrading Test and Paper trading APP
### 為什麼要用 Paper Trading

1. 學習投資技能：虛擬交易提供了一個無風險的環境，讓投資者能夠在實際市場中練習投資技能，了解投資原則和市場趨勢，學習交易策略和風險管理，提升投資技能。
2. 減少風險：使用虛擬交易可以避免使用真實資金進行投資時可能面臨的風險，如金錢損失和情緒波動。投資者可以透過虛擬交易測試不同的投資策略和風險管理方法，以找到最合適的投資方式，降低實際交易中的風險。
3. 研究市場：虛擬交易提供了一個機會，讓投資者可以研究和了解不同市場的運作方式，掌握不同金融產品的特性和投資機會，並累積實戰經驗，以做好實際投資的準備。
4. 測試新策略：投資者可以使用虛擬交易測試新的投資策略，評估其效果，並進行改進。這可以幫助投資者避免在實際市場中因新策略而產生的潛在風險，並提高投資成功的機會。

且最重要的是現行的回測軟體都要錢，且資料不易取得，因此開發此腳本


### 安裝說明

預設 python 版本: 3.8.13
使用套件:
1. backtesting
2. selenium
3. pandas
4. TA Lib
5. yfinance

#### 此工具有使用到 TA Lib 作為技術指標的工具

詳細的安裝資料可以參考
https://medium.com/ai%E8%82%A1%E4%BB%94/%E7%94%A8-python-%E5%BF%AB%E9%80%9F%E8%A8%88%E7%AE%97-158-%E7%A8%AE%E6%8A%80%E8%A1%93%E6%8C%87%E6%A8%99-26f9579b8f3a

此腳本的預設 python 版本為 3.8

若 python 版本為 3.8 則可以直接安裝 隨附的 package
安裝方法 :
pip install TA_Lib-0.4.24-cp38-cp38-win_amd64.whl

剩餘的安裝可以透過以下指令來安裝
pip install -r requirements.txt

#### 獲取最新股式資料的辦法
1. 使用 git pull 獲得此 repo 最新的股市歷史資料，此 repo 每天會進行一次資料更新

2. 透過 download.py 內建的下載資料 function 以取得最新的資料
使用方法為
python downlaod.py 或
python3 download.py

### 使用方法

#### backtestingScript 主要執行檔
backtestingScript.py 內定義了使用回測的方法
data_backtesting_with_CSI 此函數內建許多技術指標 
並且可以透過以下幾個給定的參數設定功能

1. stock_symbol 為股票代號
2. strategy 為交易策略
3. plot 是否匯出成 html 檔案, 預設產出會在 htmlPlot 資料夾內
4. start_date 為開始回測的日期，預設為 2022-01-01
5. end_date 為結束回測的日期，預設為今天
6. cash 為持有的現金 預設為 1000000
7. commission 為交易的手續費 預設為 0.001425

```python
#定義函式並執行印出物件資訊，此函式為預測 0050 股票並使用 RSI 策略並匯出成 HTML 檔案
print(data_backtesting_with_CSI('0050', strategy=RSI, plot=True))
```

於 cmd 或 powershell 內執行 python backtestingScript.py 或 python3 backtestingScript.py， 取得回測資料， 回傳物件如下

Start                     2021-03-24 00:00:00
End                       2023-04-07 00:00:00
Duration                    744 days 00:00:00
Exposure Time [%]                   67.806841
Equity Final [$]                  98462.99857
Equity Peak [$]                 118719.803722
Return [%]                          -1.537001
Buy & Hold Return [%]               -7.984791
Return (Ann.) [%]                     -0.7823
Volatility (Ann.) [%]                16.43238
Sharpe Ratio                              0.0
Sortino Ratio                             0.0
Calmar Ratio                              0.0
Max. Drawdown [%]                  -30.247341
Avg. Drawdown [%]                    -3.61419
Max. Drawdown Duration      373 days 00:00:00
Avg. Drawdown Duration       34 days 00:00:00
Trades                                     11
Win Rate [%]                        27.272727
Best Trade [%]                      18.723105
Worst Trade [%]                     -8.899368
Avg. Trade [%]                      -0.141107
Max. Trade Duration         129 days 00:00:00
Avg. Trade Duration          44 days 00:00:00
Profit Factor                        1.047737
Expectancy [%]                       0.132915
SQN                                 -0.063157
_strategy                                 RSI
_equity_curve                             ...
_trades                       Size  EntryB...
dtype: object

註: 可透過 data.py 內的公司資料來獲取想進行回測的產業和公司


#### strategies.py 交易策略

在 Strategies.py 內定義各種指標的交易策略
也可以撰寫自己的交易策略，並在 backtestingScript.py 內中呼叫
教學文章可參考:
https://havocfuture.tw/blog/python-backtesting-py

目前可直接於交易策略內獲取的指標為
1. RSI（相對強弱指標）：中文翻譯為「相對強弱指標」，是一種用於衡量市場價格變動強度和速度的技術指標，通過計算一段時間內市場上漲和下跌的平均數來判斷市場是否過度買入或過度賣出。

2. MACD（移動平均匯聚與背離指標）：中文翻譯為「移動平均匯聚與背離指標」，是一種用於判斷趨勢和市場轉折點的技術指標，通過計算兩個不同期間的移動平均線的交叉和背離來預測市場的變化。

3. KD（隨機指標）：中文翻譯為「隨機指標」，是一種用於測量市場超買和超賣情況的技術指標，通過比較當前價格和一段時間內的最高價和最低價之間的關係來判斷市場的走勢。

4. BBands（布林通道）：中文翻譯為「布林通道」，是一種用於衡量市場波動性的技術指標，通過計算一個移動平均線的標準差來建立上下兩條通道，並利用價格在通道內的位置來預測市場的變化。

詳細技術指標資訊及教學可參考
中文介紹 : https://havocfuture.tw/blog/python-indicators-talib
套件介紹 : https://github.com/TA-Lib/ta-lib-python

