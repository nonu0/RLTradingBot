import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

if not mt5.initialize():
    print('Did not launch metatrader')
    quit()

authorized = mt5.login(login=209340114,server='ExnessKE-MT5Trial9',password='19824#Thj302')
symbols = ['EURUSDm','USDJPYm','GBPUSDm','USDCHFm','AUDUSDm','USDCADm','NZDUSDm']
# for symbol in symbols:
if authorized:
    # sym = mt5.symbol_select(symbol) #bool of whether symbol is visible or not
    # account_info = mt5.symbol_info_tick('USDJPYm') # Get the current bid,ask of the symbol
    # account_info = mt5.symbol_info('USDJPYm') #all symbol info
    # date_from = datetime(2000,1,1)
    # rates = mt5.copy_rates_from(symbol,mt5.TIMEFRAME_D1,date_from,500)
    rates = mt5.copy_rates_from_pos('USDJPYm',mt5.TIMEFRAME_H1,0,24152)
    df = pd.DataFrame(rates)
    df['time'] =  pd.to_datetime(df['time'],unit='s')
    data = df.to_csv(r'C:\Users\Administrator\work\RLTrading\Bot\data\raw\1hour_data.csv',index=False)
    print(data)
# print(help(datetime))
# print(mt5.version())
# print(mt5.__dict__)
mt5.shutdown()