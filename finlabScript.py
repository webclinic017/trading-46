from finlab  import data

finlabdata = data.get('institutional_investors_trading_summary:外陸資買進股數(不含外資自營商)')
print(finlabdata)
finlabdata.to_csv('finlabdata.csv')

