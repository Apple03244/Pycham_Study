#재귀함수
#팩토리얼
import math
import pandas
#방법1
dic={}
for a in [1,1,1,1,2,2,2,2,2]:
    if a not in dic:
        dic[a]=0
    else:
        dic[a]+=1

#방법2
dic=dict.fromkeys([1,1,1,1,2,2,2,2,2],0)
for x in [1,1,1,1,2,2,2,2,2]:
    dic[x]+=1
dic

#건져갈것.
solution=lambda a:sum(map(int,list(str(a))))

#풀이 2
def solution(x,y):
    result=''
    for string in x:
        if string!=y:
            result+=string
    return result

def solution(x,y):
    return "".join([i for i in x if i!=y])

list(x).remove(y)


for i in "가나다라":
    print(i)

a="가나다라"
a.trans

#고민
20
for i in range(1,20+1):
    print(i)