import pandas as pd
import numpy as np
import datetime

#data load
D=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv')
data=pd.DataFrame(D)

#???뭐얌
data1=data.iloc[:4,:]
data2=data.iloc[4:,:]

pd.concat([data1,data2])

#92.df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
df3 = data.iloc[:2,:4]
df4 = data.iloc[5:,3:]

pd.concat([df3,df4],join='inner')

#93.df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
pd.concat([df3,df4],join='outer').fillna(0)

#94.df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
df5 = data.T.iloc[:7,:3]
df6 = data.T.iloc[6:,2:5]
df5.merge(df6,how="inner")

pd.merge(df5,df6,on="Algeria",how="inner")

#95.df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
pd.merge(df5,df6,on='Algeria',how="outer")