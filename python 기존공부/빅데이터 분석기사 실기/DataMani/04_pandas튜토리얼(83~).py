import pandas as pd
import numpy as np
import datetime

D= pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv')
data=pd.DataFrame(D)

#83.Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
data.head(2)
data.drop("Indicator",axis=1,inplace=True)
data["First Tooltip"]=data["First Tooltip"].apply((lambda x:x.split(" ")[0]))

#84.년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
idx1=data["Period"]>=2015
idx2=data["Dim1"]=="Both sexes"

data.loc[idx1&idx2]['First Tooltip'].astype("float")

#85.84번 문제에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
ans=data.loc[idx1&idx2]
ans['First Tooltip'].astype("float")
ans.groupby(["Location",'Period'])['First Tooltip'].apply(np.mean).unstack()

#86.Dim1에 따른 년도별 사망비율의 평균을 구하라
data["First Tooltip"]=data["First Tooltip"].astype("float")
data.groupby(["Dim1","Period"])['First Tooltip'].mean().unstack()