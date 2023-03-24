from datetime import datetime
import backtrader as bt
import yfinance as yf
import time
# 定義一個Indicator物件
class DonchianChannels(bt.Indicator):
    # 這個物件的別名，所以後面我們可以用DCH/DonchianChannel來呼叫這個指標
    alias = ('DCH', 'DonchianChannel',)
    
    # 三條線分別代表唐奇安通道中的 中軌(上軌加下軌再除以2)、上軌、下軌
    lines = ('dcm', 'dch', 'dcl',)  # dc middle, dc high, dc low
    
    # 軌道的計算方式：用過去20天的資料來計算，所以period是20，lookback的意思是要不要將今天的資料納入計算，由於唐奇安通道是取過去20天的最高或最低，所以一定不能涵蓋今天，不然永遠不會有訊號出現，所以要填-1(從前一天開始算20天)
    params = dict(
        period=20,
        lookback=-1,  # consider current bar or not
    )
    
    # 是否要將Indicators另外畫一張圖，然而通道線通常都是跟股價圖畫在同一張，才能看得出相對關係，所以這裡就填subplot=False
    plotinfo = dict(subplot=False)  # plot along with data
    
    # 繪圖設定，ls是line style，'--'代表虛線
    plotlines = dict(
        dcm=dict(ls='--'),  # dashed line
        dch=dict(_samecolor=True),  # use same color as prev line (dcm)
        dcl=dict(_samecolor=True),  # use same color as prev line (dch)
    )
    
    def __init__(self):
        # hi與lo是指每日股價的最高與最低價格
        hi, lo = self.data.high, self.data.low
        
        # 視需求決定是否要從前一天開始讀資料，上面已經定義lookback存在，所以這邊會直接從前一天的資料開始跑
        if self.p.lookback:  # move backwards as needed
            hi, lo = hi(self.p.lookback), lo(self.p.lookback)
        
        # 定義三條線的計算方式
        self.l.dch = bt.ind.Highest(hi, period=self.p.period)
        self.l.dcl = bt.ind.Lowest(lo, period=self.p.period)
        self.l.dcm = (self.l.dch + self.l.dcl) / 2.0  # avg of the above

class MyStrategy(bt.Strategy):
    def __init__(self):
        # DCH就是上面定義的 DonchianChannels的alias
        self.myind = DonchianChannels()

    def next(self):
        if self.data[0] > self.myind.dch[0]:
            self.buy()
        elif self.data[0] < self.myind.dcl[0]:
            self.sell()




# cerebro = bt.Cerebro()
# cerebro.addstrategy(MyStrategy)
# cerebro.broker.setcash(1000)
# cerebro.broker.setcommission(commission=0.001)

# data = bt.feeds.PandasData(dataname=yf.download("3481.TW", start="2020-01-01", end="2023-03-24"))

# cerebro.adddata(data)
# print('Starting Value: %.2f' % cerebro.broker.getvalue())
# cerebro.run()
# print('Ending Value: %.2f' % cerebro.broker.getvalue())
# cerebro.plot()

# "data ="[
#    "2301 光寶科",
#    "2302 麗正",
#    "2303 聯電",
#    "2305 全友",
#    "2308 台達電子",
#    "2310 旭麗",
#    "2311 日月光",
#    "2312 金寶",
#    "2313 華通",
#    "2314 台揚",
#    "2315 神達",
#    "2316 楠梓電子",
#    "2317 鴻海",
#    "2318 佳錄",
#    "2319 大眾",
#    "2321 東訊",
#    "2322 致福",
#    "2323 中環",
#    "2324 仁寶",
#    "2325 矽品",
#    "2326 亞瑟",
#    "2327 國巨",
#    "2328 廣宇",
#    "2329 華泰",
#    "2330 台積電",
#    "2331 精英",
#    "2332 友訊",
#    "2333 碧悠",
#    "2335 清三",
#    "2336 致伸",
#    "2337 旺宏",
#    "2338 光罩",
#    "2339 合泰",
#    "2340 光磊",
#    "2341 英群",
#    "2342 茂矽",
#    "2343 精業",
#    "2344 華邦電子",
#    "2345 智邦",
#    "2347 聯強",
#    "2348 力捷",
#    "2349 錸德",
#    "2350 環電",
#    "2351 順德",
#    "2352 明基",
#    "2353 宏碁",
#    "2354 華升",
#    "2355 敬鵬",
#    "2356 英業達",
#    "2357 華碩",
#    "2358 美格",
#    "2359 所羅門",
#    "2360 致茂",
#    "2361 鴻友",
#    "2362 藍天",
#    "2363 矽統",
#    "2364 倫飛",
#    "2365 昆盈",
#    "2366 亞旭",
#    "2367 燿華",
#    "2368 金像電子",
#    "2369 菱生",
#    "2370 匯僑工業",
#    "2371 大同",
#    "2373 震旦行",
#    "2374 佳能",
#    "2375 智寶",
#    "2376 技嘉",
#    "2377 微星",
#    "\"2378 鴻運"
tech = [
    ['2301.TW', '光寶科'],
    ['2302.TW', '麗正'],
    ['2303.TW', '聯電'],
    ['2305.TW', '全友'],
    ['2308.TW', '台達電子'],
    ['2310.TW', '旭麗'],
    ['2311.TW', '日月光'],
    ['2312.TW', '金寶'],
    ['2313.TW', '華通'],
    ['2314.TW', '台揚'],
    ['2315.TW', '神達'],
    ['2316.TW', '楠梓電子'],
    ['2317.TW', '鴻海'],
    ['2318.TW', '佳錄'],
    ['2319.TW', '大眾'],
    ['2321.TW', '東訊'],
    ['2322.TW', '致福'],
    ['2323.TW', '中環'],
    ['2324.TW', '仁寶'],
    ['2325.TW', '矽品'],
    ['2326.TW', '亞瑟'],
    ['2327.TW', '國巨'],
    ['2328.TW', '廣宇'],
    ['2329.TW', '華泰'],
    ['2330.TW', '台積電'],
    ['2331.TW', '精英'],
    ['2332.TW', '友訊'],
    ['2333.TW', '碧悠'],
    ['2335.TW', '清三'],
    ['2336.TW', '致伸'],
    ['2337.TW', '旺宏'],
    ['2338.TW', '光罩'],
    ['2339.TW', '合泰'],
    ['2340.TW', '光磊'],
    ['2341.TW', '英群'],
    ['2342.TW', '茂矽'],
    ['2343.TW', '精業'],
    ['2344.TW', '華邦電子'],
    ['2345.TW', '智邦'],
    ['2347.TW', '聯強'],
    ['2348.TW', '力捷'],
    ['2349.TW', '錸德'],
    ['2350.TW', '環電'],
    ['2351.TW', '順德'],
    ['2352.TW', '明基'],
    ['2353.TW', '宏碁'],
    ['2354.TW', '華升'],
    ['2355.TW', '敬鵬'],
    ['2356.TW', '英業達'],
    ['2357.TW', '華碩'],
    ['2358.TW', '美格'],
    ['2359.TW', '所羅門'],
    ['2360.TW', '致茂'],
    ['2361.TW', '鴻友'],
    ['2362.TW', '藍天'],
    ['2363.TW', '矽統'],
    ['2364.TW', '倫飛'],
    ['2365.TW', '昆盈'],
    ['2366.TW', '亞旭'],
    ['2367.TW', '燿華'],
    ['2368.TW', '金像電子'],
    ['2369.TW', '菱生'],
    ['2370.TW', '匯僑工業'],
    ['2371.TW', '大同'],
    ['2373.TW', '震旦行'],
    ['2374.TW', '佳能'],
    ['2375.TW', '智寶'],
    ['2376.TW', '技嘉'],
    ['2377.TW', '微星'],
    ['2378.TW', '鴻運'],
    ['2379.TW', '瑞昱'],
    ['2380.TW', '威盛'],
    ['2381.TW', '旭隼'],
    ['2382.TW', '廣達'],
    ['2383.TW', '群光'],
    ['2384.TW', '鴻準'],
    ['2385.TW', '威盛-KY'],
    ['2386.TW', '瀚宇博'],
    ['2387.TW', '精元'],
    ['2388.TW', '威盛2'],
    ['2389.TW', '瑞昱2'],
    ['2390.TW', '瑞昱3'],
    ['2391.TW', '瑞昱4'],
    ['2392.TW', '瑞昱5'],
    ['2393.TW', '瑞昱6'],
    ['2394.TW', '瑞昱7'],
    ['2395.TW', '瑞昱8'],
    ['2396.TW', '瑞昱9'],
    ['2397.TW', '瑞昱10'],
    ['2398.TW', '瑞昱11'],
    ['2399.TW', '瑞昱12']
]
cloth = [
    ['1402.TW' ,'遠紡'],
    ['1407.TW', '華隆'],
    ['1408.TW', '中紡'],
    ['1409.TW', '新纖'],
    ['1410.TW', '南染'],
    ['1413.TW' ,'宏洲'],
    ['1414.TW' ,'東和'],
    ['1416.TW', '廣豐'],
    ['1417.TW', '嘉裕'],
    ['1418.TW', '東華'],
    ['1419.TW', '新紡'],                 
    ['1423.TW' ,'利華'],
    ['1432.TW', '大魯閣'],
    ['1434.TW', '福懋'],
    ['1435.TW', '中福'],
    ['1436.TW', '福益'],
    ['1437.TW' ,'勤益'],
    ['1438.TW', '裕豐'],
    ['1439.TW' ,'中和'],
    ['1440.TW', '南紡'],
]
average = []

for company in tech:
    try:
        cerebro = bt.Cerebro()
        cerebro.broker.setcash(1000)
        cerebro.broker.setcommission(commission=0.001)
        cerebro.addstrategy(MyStrategy)

        data = bt.feeds.PandasData(dataname=yf.download(company[0], start="2022-01-01", end="2023-03-24"))
        print('公司名稱:',company[1])
        cerebro.adddata(data)
        cerebro.run()
        print('Ending Value: %.2f' % cerebro.broker.getvalue())
        average.append(cerebro.broker.getvalue())
        time.sleep(2)
    except:
        pass
print('平均值:',sum(average)/len(average))
    