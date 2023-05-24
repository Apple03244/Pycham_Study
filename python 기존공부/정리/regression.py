#regression
import pandas as pd
import os

D=pd.read_csv('C:/Users/SAMSUNG/파이썬 스터디//Boston_house.csv')
data=pd.DataFrame(D)

import statsmodels.api as sm
import statsmodels.formula.api as smf

data
#단순회귀 분석
target=data['Target']
target #주택 중앙값
crim=data['CRIM']
crim #인구중 흑인 비율
rm=data['RM']


#선형성 확인
import matplotlib.pyplot as plt

plt.scatter(rm,target,label="Data")
plt.plot(rm,pred1,label="predict")
plt.show()
#선형성 확인 완료

rm1=sm.add_constant(rm)
r_model=sm.OLS(target,rm1)
fitmodel=r_model.fit()

pred1=fitmodel.predict(rm1)
