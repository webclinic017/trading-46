#       1. Open 
#   2. High 
#   3. Low 
#   4. Close 
#   5. Adj Close 
#   6. Volume 
#   7. slowk 
#   8. slowd 
#   9. macd 
#   10. macdsignal 
#   11. macdhist 
#   12. RSI 
#   13. upperband 
#   14. middleband 
#   15. lowerband

def BacktestParams(input):
    try:
        # output = int(input)
        # rounded_output = round(output/100,2)
        # return rounded_output
        return int(input)
    except ValueError:
        pass
    
    backtest_compare = {
        'crossover': 'crossover',
        '<':'<',
        '>':'>',
        '<=':'<=',
        '>=':'>=',
        '==':'==',
        '!=':'!=',
    }
    
    backtest_params = {
        'slowk': 'self.data.slowk',
        'slowd': 'self.data.slowd',
        'macd': 'self.data.macd',
        'macdsignal': 'self.data.macdsignal',
        'macdhist': 'self.data.macdhist',
        'RSI': 'self.data.RSI',
        'upperband': 'self.data.upperband',
        'middleband': 'self.data.middleband',
        'lowerband': 'self.data.lowerband',
        'Open': 'self.data.Open',
        'High': 'self.data.High',
        'Low': 'self.data.Low',
        'Close': 'self.data.Close',
        'Adj Close': 'self.data.Adj Close',
        'Volume': 'self.data.Volume',
    }
    if input in backtest_params:
        return backtest_params[input]
    elif input in backtest_compare:
        return backtest_compare[input]
    else:
        return False   



