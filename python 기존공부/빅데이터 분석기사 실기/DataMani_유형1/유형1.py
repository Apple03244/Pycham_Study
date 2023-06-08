import pandas as pd
D=pd.read_csv(r'https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv'
              ,index_col="Unnamed: 0")
data=pd.DataFrame(D)

data.describe()
data.columns
data["channelTitle"]
#1.인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
#step_1: 인기동영상 제작횟수 정리
answer=['장삐쭈', '총몇명', '파뿌리', '짤툰', '런닝맨 - 스브스 공식 채널', '엠뚜루마뚜루 : MBC 공식 종합 채널', 'SPOTV', '채널 십오야', '이과장', 'BANGTANTV']
set(data.channelTitle.value_counts().head(10).index)==set(answer)

#2.논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 like 수보다 높은 동영상을 제작한 채널을 모두 출력하라
#step_1: dislike와 like 비교
data['step1']=data.dislikes-data.likes
#step2. 논란 추출
idx=data.step1>0
set(data.loc[idx,'channelTitle'])==set(answer)
answer=['핫도그TV', 'ASMR 애정TV', '하얀트리HayanTree', '양팡 YangPang', '철구형 (CHULTUBE)', '왜냐맨하우스', '(MUTUBE)와꾸대장봉준', '오메킴TV', '육지담', 'MapleStory_KR', 'ROAD FIGHTING CHAMPIONSHIP', '사나이 김기훈', '나혼자산다 STUDIO', 'Gen.G esports']

#3.채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
#step1.channelID를 기준으로 보자
idx=data.groupby(['channelId'])['channelTitle'].nunique()
#step2
idx[idx>1].count()

#4.일요일에 인기있었던 영상들중 가장많은 영상 종류(categoryId)는 무엇인가?
#step1.
data['trending_date2']=data['trending_date2'].apply(lambda x:pd.to_datetime(x).weekday())
idx=data['trending_date2']==6
answer=pd.DataFrame(data.loc[idx,'categoryId'].value_counts())
answer.iloc[0]

#5.각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
#step1.요일별 이름으로 바꿈
data['trending_date2']=data['trending_date2'].apply(lambda x:pd.to_datetime(x).day_name())
#step2.groupby
data.groupby(['categoryId','trending_date2']).size().unstack()

#6.댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다. viewcount대비 댓글수가 가장 높은 영상을 확인하라 (view_count값이 0인 경우는 제외한다)
pre_data=data.copy()
pre_data.view_count.dropna()
pre_data['temp']=pre_data.comment_count/pre_data.view_count
pre_data.sort_values(by='temp',ascending=True).iloc[0].title

pre_data=pre_data.loc[pre_data.view_count!=0]

#7.댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다.viewcount대비 댓글수가 가장 낮은 영상을 확인하라 (view_counts, ratio값이 0인경우는 제외한다.)
pre_data=data.copy()
pre_data=pre_data.loc[data.view_count!=0]
pre_data['ratio']=pre_data.comment_count/pre_data.view_count
test=pre_data.loc[pre_data.ratio!=0]
test.sort_values(by='ratio').title.iloc[0]

#8.like 대비 dislike의 수가 가장 적은 영상은 무엇인가? (like, dislike 값이 0인경우는 제외한다
pre_data=data.copy()
idx=pre_data.dislikes!=0
idx2=pre_data.likes!=0
test=pre_data.loc[(idx)&(idx2)].dropna()
test["ratio"]=test['dislikes']/pre_data['likes']
test[test.ratio.sort_values().index[0]]

