#statsmodel vs sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#data
D=pd.read_csv('C:/Users/SAMSUNG/파이썬 스터디/Boston_house.csv')
data=pd.DataFrame(D)

#One Linear Regression
#데이터 선정하겠습니다

data.head()
data.info()
T_data=data['Target']
rm=data['RM']

#선형성을 확인해야하는데..
plt.scatter(rm,T_data)
plt.show()

#방법 1. statsmodel
import statsmodels.api as sm
import statsmodels.formula.api as smf

#무조건 상수 추가를 해야한다잉
add_rm=sm.add_constant(rm)

model=sm.OLS(T_data,add_rm)
fit_md=model.fit()
pre1=fit_md.predict(add_rm)

#히히..꾸며볼까?
plt.title("RM-Target")
plt.scatter(rm,T_data,label="data")
plt.plot(rm,pre1,'r-',label='statsmodel')
plt.xlabel("RM")
plt.ylabel("Target")
plt.legend()
plt.show()

#방법2. 싸이킷 런
from sklearn.linear_model import LinearRegression

model=LinearRegression()
model.fit(rm1.reshape(-1,1),T_data)

#간단하지만 x의 reshape이 필요함. 즉 array로 바꿔야함!!
rm1=np.array(rm)
rm1.reshape(-1,1)

#위의 과정을 끝냈으면
pre2=model.predict(rm1.reshape(-1,1))

#히히..꾸며볼까? #둘다 확인할 수 있게!!
plt.title("RM-Target")
plt.scatter(rm,T_data,label="data")
plt.plot(rm,pre1,'r-',label='statsmodel')
plt.plot(rm,pre2,'b-',label="sklearn")
plt.xlabel("RM")
plt.ylabel("Target")
plt.legend()
plt.show()

#비교해보자
#fit_md:statsmodel, model:sklearn

fit_md.summary() #R_squares : 0.484
#sklearn 패키지는 summary 제공 ㄴㄴ

#잔차(residual)
