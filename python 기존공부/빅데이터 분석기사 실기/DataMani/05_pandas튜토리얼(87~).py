import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv')
data=pd.DataFrame(df)

#87.데이터에서 한국 KOR 데이터만 추출하라
data.tail()
idx=data["Country"]=="KOR"
data.loc[idx]

#88.한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
test=data.loc[idx]
test.groupby(['Year','Medal']).size().unstack().fillna(0)

#89.전체 데이터에서 sport종류에 따른 성별수를 구하여라
data.groupby(['Sport','Gender']).size().unstack()

#90.전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
data.groupby(["Discipline",'Medal']).size().unstack().fillna(0)

#91.