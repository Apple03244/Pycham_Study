#road data
import pandas as pd
D=pd.read_csv("C:/Users/SAMSUNG/Desktop/빅데이터 분석기사/games.csv")

#3.데이터 행렬 개수
D.shape

#4.print columns
D.columns

#5.6번째 컬럼 호출
D[D.columns[5]]

#6.데이터 타입 호출
D[D.columns[5]].dtype

#7.데이터 타입의 인덱스 구성은 어떤가?
D.index

#8.6번째 컬럼의 3번째 값은 무엇인가
D[D.columns[5]].iloc[2]
D.iloc[2,5]

#9.데이터 로드 #한글은 오류가 남. encoding='euc_kr
D=pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv',encoding='euc_kr')

#10.마지막 3개의 행을 출력해라
D.tail(3)

#11.수치형변수를 가진 칼럼을 호출해라
ind=D.dtypes!='object'
D.columns[ind]

D.select_dtypes(exclude='object').columns

#12.범주형 데이터형태를 가진 컬럼을 호출하라
D.select_dtypes(include='object').columns

#13.각 컬럼의 nan 값을 출력해라
idx=D.isna()==True
D[idx].count()

D.isna().sum()

#14.각 컬럼의 데이터 수,데이터 타입을 확인하라
D.info()
ind=D.dtypes!='object'

#15.각 수치형 변수의 분포를 확인하라
D.select_dtypes(exclude='object').describe()

#16.거주 인구의 컬럼값들을 출력해라
D['평균 속도'].quantile(0.75)-D['평균 속도'].quantile(0.25)

#17.읍면동명 컬럼의 유일값 갯수를 구하라.
len(D['읍면동명'].unique())

D['읍면동명'].nunique()

#18.위의 유일값들을 출력하라
D['읍면동명'].unique()

#20.데이터 로드
D=pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv')

#21.quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라
ix=D["quantity"]==3
D[ix].head(5)

#22.quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라
D[ix].reset_index(drop=True)

#23.quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라
data=pd.DataFrame(D,columns=['quantity','item_price'])
data

#24.item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라
data['new_price']=data['item_price'].apply(lambda x:float(x[1:]))

data['new_price2']=data['item_price'].str[1:].astype(str)

#25.new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라
data.drop('new_price2',axis=1,inplace=True)
len(data[data['new_price']<=5])

#26.item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하라고 index 값을 초기화 하여라
data2=D[D['item_name']=='Chicken Salad Bowl'].reset_index(drop=True)
data2

#27.new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
data2["new_price"]=data['item_price'].apply(lambda x:float(x[1:]))
idx=data2['new_price']<=9
idx2=data2['item_name']=='Chicken Salad Bowl'
data2[idx & idx2]
data2.loc[(data2.item_name =='Chicken Salad Bowl') & (data2.new_price <= 9)]

#28.df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
data.sort_values('new_price',ascending=False).reset_index(drop=True)

#29.df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
D[D['item_name']=='Chips']

#30.df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
D[D.columns[range(1,len(D.columns),2)]]

D.iloc[:,::2]

#31.df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
D['new_price']=D['item_price'].apply(lambda x:float(x[1:]))
D.set_index('new_price').sort_index(ascending=False)

#32.df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
s1=D[D['item_name']=='Steak Salad']
s2=D[D['item_name']=='Bowl']
s3=pd.concat([s1,s2]).sort_index()
s3
D[(D['item_name']=='Steak Salad')|(D['item_name']=='Bowl')] #시발

#33.df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
pd.DataFrame([s1.iloc[0],s2.iloc[0]])
s3.drop_duplicates('item_name')

#34.df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
pd.DataFrame([s1.iloc[-1],s2.iloc[-1]])
s3.drop_duplicates('item_name',keep='last')

#35.df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
D[D['new_price']>=(D['new_price'].mean())]

#36.df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
D=D.apply(lambda x:x.replace("Izze","Fizzy Lizzy"))

D.loc[D['item_name']=='Izze','item_name']='Fizzy Lizzy'

#37.df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
D['choice_description'].isna().sum()

#38.df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
D.loc[D['choice_description'].isna(),'choice_description']='NoData'
D['choice_description']

#39.df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
D[D['choice_description'].apply(lambda x:x.find('Black')!=-1)]

'1234'.__contains__('1')

#40.df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
D['choice_description'].apply(lambda x:x.find('Vegetables')==-1).sum()

#41.df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
idx=D['item_name'].apply(lambda x:x[0]=="N")
D.loc[idx]

#42.df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
idx=D['item_name'].apply(lambda x:len(x)>=15)
D.loc[idx]

#43.df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
D['new_price']=D.item_price.str[1:].astype(float)
D[D['new_price'].apply(lambda x:x in lst)]
D['new_price'].apply(lambda x:x in lst).sum()



