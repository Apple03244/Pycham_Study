import pandas as pd
import numpy as np
import datetime

#64. data load
D=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv')
data=pd.DataFrame(D)
data.head(2)

#65.Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
data['Yr_Mo_Dy']=data['Yr_Mo_Dy'].astype(dtype='datetime64[ns]')

#66.Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
a=data['Yr_Mo_Dy']
A=a.apply(lambda x:str(x).split("-")[0])
A.unique()

data['Yr_Mo_Dy'].dt.year.unique() #오...

#67.Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
idx=data['Yr_Mo_Dy'].dt.year>=2061
data.loc[idx,'Yr_Mo_Dy']=data[idx]['Yr_Mo_Dy'].apply(lambda x:pd.to_datetime(datetime.date(x.year-100,x.month,x.day)))
data['Yr_Mo_Dy']

#68.년도별 각컬럼의 평균값을 구하여라
data.groupby(data['Yr_Mo_Dy'].dt.year).mean()

#69.weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
dic=dict(zip(range(7),['월','화','수','목','금','토','일'])
data.Yr_Mo_Dy.dt.day.apply(lambda x:dic[x%7])

data.Yr_Mo_Dy.dt.weekday

#70.weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
data.Yr_Mo_Dy.dt.weekday.apply(lambda x:1 if x in [5,6] else 0)

#71.년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
data.groupby(data.Yr_Mo_Dy.dt.month).mean()

#72.모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
inx=data.isna()==True
data.fillna(method='ffill').fillna(method='bfill')

#73.년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
data.groupby([data.Yr_Mo_Dy.dt.year,data.Yr_Mo_Dy.dt.month]).mean().unstack()

data.groupby(data.Yr_Mo_Dy.dt.to_period('M')).mean()
data.groupby()

#RPT 컬럼의 값을 일자별 기준으로 1차차분하라
data['RPT'].diff()