import numpy as np
import pandas as pd
import pandas_datareader.data as web


sp500 = web.DataReader('^GSPC', 'yahoo', start='1/1/2000', end = '5/3/2016')

sp500.info()

sp500['42d'] = pd.rolling_mean(sp500['Close'], window =42)
sp500['252d'] = pd.rolling_mean(sp500['Close'], window = 252)
sp500[['Close', '42d', '252d']].tail()
 
sp500[['Close', '42d', '252d']].plot(grid = True, figsize = (8,5))

#Buy Signal ; 42d trend is for the first time SD points above 252d trend
#Wait(park in cash) : 42d trend is within a range of +/- SD points around the 252d trend
#Sell (go short): 42d trend is for the first time SD points below the 252d trend. 

sp500['42-252'] = sp500['42d'] - sp500['252d']
sp500['42-252'].tail()

SD = 50

sp500['Regime'] = np.where(sp500['42-252'] > SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252'] <-5, -1, sp500['Regime'])

sp500['Regime'].value_counts()

sp500['Regime'].plot(lw=1.5)(subplot(True), grid=True, style='b', figsize=(8,6))
#ylim([-1.1, 1.1])
