#44.데이터 로드
import pandas as pd
import numpy as np

D=pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv')
D.head(5)
d=pd.DataFrame(D)

#45.데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라
d.groupby('host_name').count().sort_index().head(5)

#46.데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라
ans=pd.DataFrame(d.groupby('host_name').count(),columns=['id'])
ans.sort_values(['id'],ascending=False)
ans.rename(columns={'id':'counts'},inplace=True)
ans.sort_values(['counts'],ascending=False).head(5)

'''#transform 함수를 기억하자
d.groupby('host_name').mean()
d['temp']=d.groupby('host_name').transform('count')['id']
d.head()
d.drop('temp',axis=1)
'''

#47.neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라
d.columns
data=pd.DataFrame(d.groupby(['neighbourhood_group',"neighbourhood"]).count()['id'])

#48.neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라
d.groupby(['neighbourhood_group', 'neighbourhood'], as_index=False).size().groupby(['neighbourhood_group'], as_index=False).max()

d.groupby(['neighbourhood_group', 'neighbourhood'],as_index=False).size().groupby(['neighbourhood_group']).max()

#49.neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
d[['neighbourhood_group','price']].groupby(['neighbourhood_group']).agg(['min','max','var','mean'])

#50.neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
d[['neighbourhood_group','reviews_per_month']].groupby(['neighbourhood_group']).agg(['min','max','var','mean'])

#51.neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라
d[['neighbourhood','neighbourhood_group','price']].groupby(['neighbourhood','neighbourhood_group']).mean()

#52.neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라
d['price_mean']=d.groupby(['neighbourhood','neighbourhood_group'])['price'].transform(np.mean)

#시발..
d.groupby(['neighbourhood','neighbourhood_group'])['price'].mean().unstack()

#53.neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고 nan 값은 -999값으로 채워라
d.groupby(['neighbourhood','neighbourhood_group'])['price'].mean().unstack().fillna("-999")

#54.데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라
d.loc[d['neighbourhood_group']=='Queens'].groupby('neighbourhood')['price'].agg(['min','max','var','mean'])

#55.데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고 neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라
ans=pd.DataFrame(d.groupby(['neighbourhood_group','room_type']).size().unstack())
temp=d.groupby(['neighbourhood_group'])['room_type'].size()
ans.apply(lambda x:x/temp)