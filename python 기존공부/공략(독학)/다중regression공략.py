#변수가 하나가 아니면?
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

#데이터
D=pd.read_csv('C:/Users/SAMSUNG/파이썬 스터디/Boston_house.csv')
data=pd.DataFrame(D)

#데이터 분할 하자잉
target=data[["Target"]]
crim=data[["CRIM"]]
rm=data[["RM"]]
lstat=data[["LSTAT"]]

#선형성 확인하자
import matplotlib.pyplot as plt
#subplot 이용
dic=dict(zip([131,132,133],[crim,rm,lstat]))

for i,j in dic.items():
    plt.subplot(i)
    plt.scatter(j, target)
plt.show()

#참고사항 : seaborn 이용하기
import seaborn as sns

fig, axs = plt.subplots(figsize=(15, 5), ncols=4, nrows=2)
lm_features = data[['CRIM','RM','LSTAT','TAX','AGE','ZN','NOX','INDUS']]

for i, feature in enumerate(lm_features):
    row = int(i/4)
    col = i%4
    sns.regplot(x=feature, y='Target', data=data, ax=axs[row][col])

#Multi Linear Regression
multi=data[['CRIM','RM','LSTAT']]
multi.head(2)
use_multi=sm.add_constant(multi)
MLR=sm.OLS(target,use_multi)
model=MLR.fit()

model.params #기울기 확인
model.summary() #결과 확인
#잔차 확인
model.resid.plot()
plt.show()


