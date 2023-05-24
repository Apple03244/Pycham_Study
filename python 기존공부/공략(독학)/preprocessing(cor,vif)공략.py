#데이터 전처리
import pandas as pd

D=pd.read_csv('C:/Users/SAMSUNG/파이썬 스터디/Boston_house.csv')
data=pd.DataFrame(D)

#다중공산성
use_data=data[data.columns.difference(['Target'])]
use_data.corr()

#시각화
import seaborn as sns

cmap=sns.light_palette('darkgrey',as_cmap=True)
sns.heatmap(use_data.corr(),cmap=cmap,annot=True,cbar=True)
plt.show()

#산점도 : 분포도이니까 데이터의 대강의 모습만 보는거지
sns.pairplot(use_data)
plt.show()

#VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor
VIF=pd.DataFrame()
VIF['Features']=use_data.columns
VIF['VIF']=[variance_inflation_factor(use_data.values,i) for i in range(use_data.shape[1])]
VIF

use_data1=use_data.drop(["PTRATIO"],axis=1)
VIF1=pd.DataFrame()
VIF1['Features']=use_data1.columns
VIF1['VIF']=[variance_inflation_factor(use_data1.values,i) for i in range(use_data1.shape[1])]
VIF1

use_data2=use_data1.drop(['NOX'],axis=1)
VIF2=pd.DataFrame()
VIF2['Features']=use_data2.columns
VIF2['VIF']=[variance_inflation_factor(use_data2.values,i) for i in range(use_data2.shape[1])]
VIF2

use_data3=use_data2.drop(['TAX'],axis=1)
VIF3=pd.DataFrame()
VIF3['Features']=use_data3.columns
VIF3['VIF']=[variance_inflation_factor(use_data3.values,i) for i in range(use_data3.shape[1])]
VIF3

#이정도면 그만 지우자
