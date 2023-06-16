import numpy as np
import pandas as pd

D=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/datarepo/main/bicycle/seoul_bi.csv')
df=pd.DataFrame(D)

#31.대여일자별 데이터의 수를 데이터프레임으로 출력하고, 가장 많은 데이터가 있는 날짜를 출력하라.
df["대여일자"]
