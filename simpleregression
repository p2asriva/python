import pandas as pd
from scipy import *
from numpy import *
#import statsmodels.api as sm

#path = 'M:/Pittsburgh/GRP2/MRM_Systems/Regular and Ongoing/Models/MEC/Production/2016/2016.Q1/Input Files/'
path = 'L:/PyProjects/'

# read in the following format for the dates to be recognised as dates. index_col=0 does that

es2=pd.read_csv(path+'BLK_Market_Data.csv', parse_dates=True, index_col=0, dayfirst=True)
es2.plot(subplots= True, grid=True, style='b', figsize=(8,6))  # notice the difference from es plot

rfr_daily=(1+es2["H15T1Y Index"]/100)**(1/365)-1

rets=(es2/es2.shift(7))-1

rets.plot(subplots= True, grid=True, style='b', figsize=(8,6))

mrp=4.93778754603691

rets['SPXT Index']-= rfr_daily
rets['BLK Equity']-= rfr_daily

CMT1Y= es2['H15T1Y Index'][-1]

# regress blk excess returns over s&P returns minus risk premium

model = pd.ols(y=rets['BLK Equity'], x=rets['SPXT Index'] )
model
myReturn=CMT1Y+model.beta.x*mrp
