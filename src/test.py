import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\Administrator\work\RLTrading\Bot\data\raw\1hour_data.csv')
df = pd.DataFrame(data)
# print(df.info())
# print(df.describe())
df.drop(['real_volume'],axis=1,inplace=True)
df['log_returns'] = np.log(df['close']/df['close'].shift(1))
# new_df = df.drop(['open','high','low','close','tick_volume'])
df.to_csv(r'C:\Users\Administrator\work\RLTrading\Bot\data\processed\processed.csv')
print(df)
