import numpy as np
import pandas as pd
from datetime import datetime,date


D=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/datarepo/main/bicycle/seoul_bi.csv')
df=pd.DataFrame(D)

#31.대여일자별 데이터의 수를 데이터프레임으로 출력하고, 가장 많은 데이터가 있는 날짜를 출력하라.
df.groupby('대여일자')["대여일자"].count().sort_values(ascending=False).head(1)

#32.각 일자의 요일을 표기하고 (‘Monday’ ~’Sunday’) ‘day_name’컬럼을 추가하고 이를 이용하여 각 요일별 이용 횟수의 총합을 데이터 프레임으로 출력하라
df['대여일자']=df['대여일자'].apply(lambda x:pd.to_datetime(x))
df['day_name']=df.대여일자.apply(datetime.weekday)
df['day_name']=df.day_name.apply(lambda x:wkday[x])
df.groupby("day_name")['대여일자'].count()
wkday='월화수목금토일'

#33.각 요일별 가장 많이 이용한 대여소의 이용횟수와 대여소 번호를 데이터 프레임으로 출력하라
answer=pd.DataFrame(df.groupby("day_name")["대여소번호"].value_counts().sort_values(ascending=False))

#34.나이대별 대여구분 코드의 (일일권/전체횟수) 비율을 구한 후 가장 높은 비율을 가지는 나이대를 확인하라. 일일권의 경우 일일권 과 일일권(비회원)을 모두 포함하라
df.head()
answer=pd.DataFrame(df.groupby('연령대코드')["대여구분코드"].value_counts().sum()).unstack().reset_index()
answer