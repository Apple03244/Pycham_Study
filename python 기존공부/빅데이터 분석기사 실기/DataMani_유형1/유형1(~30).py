import pandas as pd
import numpy as np

D=pd.read_csv(r"https://raw.githubusercontent.com/Datamanim/datarepo/main/worldcup/worldcupgoals.csv")
data=pd.DataFrame(D)
#21.주어진 전체 기간의 각 나라별 골득점수 상위 5개 국가와 그 득점수를 데이터프레임형태로 출력하라
answer=data.groupby("Country")['Goals'].sum().sort_values(ascending=False)
answer.head(5)

#22.주어진 전체기간동안 골득점을 한 선수가 가장 많은 나라 상위 5개 국가와 그 선수 숫자를 데이터 프레임 형식으로 출력하라
answer=data.groupby('Country')['Player'].count().sort_values(ascending=False)
answer

#23.Years 컬럼은 년도 -년도 형식으로 구성되어있고, 각 년도는 4자리 숫자이다. 년도 표기가 4자리 숫자로 안된 케이스가 존재한다. 해당 건은 몇건인지 출력하라
answer=data['Years'].apply(lambda x:x.split("-"))
def count(x):
    for year in x:
        if len(year)!=4:
            return 1
    return 0
data['temp']=answer.apply(count)
data['temp']
#24.**Q3에서 발생한 예외 케이스를 제외한 데이터프레임을 df2라고 정의하고 데이터의 행의 숫자를 출력하라 (아래 문제부터는 df2로 풀이하겠습니다) *
df2=data.loc[data['temp']==0]
df2['Player'].count()
df2.Years
#25.월드컵 출전횟수를 나타내는 ‘LenCup’ 컬럼을 추가하고 4회 출전한 선수의 숫자를 구하여라
df2.insert(5,"temp2",df2.Years.apply(lambda x:len(x.split("-"))),allow_duplicates=False)
df2.rename(columns={"temp2":'LenCup'},inplace=True)
df2.drop(labels=['temp'],axis=1,inplace=True)
df2.loc[df2.LenCup>=4,'Player'].count()

#26.Yugoslavia 국가의 월드컵 출전횟수가 2회인 선수들의 숫자를 구하여라
df2.loc[(df2.LenCup==2)&(df2.Country=="Yugoslavia")]['Player'].count()

#27.2002년도에 출전한 전체 선수는 몇명인가?
df2.Years.apply(lambda x: True if "2002" in x else False).sum()

#28.이름에 ‘carlos’ 단어가 들어가는 선수의 숫자는 몇 명인가? (대, 소문자 구분 x)
df2.Player.apply(lambda x: True if "carlos" in x.lower() else False).sum()

#29.월드컵 출전 횟수가 1회뿐인 선수들 중에서 가장 많은 득점을 올렸던 선수는 누구인가?
df2.loc[df2.LenCup==1].sort_values("Goals").tail(1).Player

#30.월드컵 출전횟수가 1회 뿐인 선수들이 가장 많은 국가는 어디인가?
df2.loc[df2.LenCup==1,'Country'].value_counts().head(1)
