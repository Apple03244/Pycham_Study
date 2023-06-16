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

#효율성
from collections import Counter
a=[1,1,1,1,1,2,2,2,2,2,3,3,4]
result={}
for i in a:
    if i not in result:
        result[i]=1
    else:
        result[i]+=1
result
Counter(a)



a=1234
result=0
if a>=1:
    result+=1
if a>=10:
    result+=1
if a>=100:
    result+=1
else:
    result+=1

print(result)

import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
a=[[1,2,3],[4,5,6]]
a[0][1]
A[0,1]
type(A)
id=A>=4
A[A>=4]
temp=#1번째에서 뽑은 작은 숫자


#깊은 복사, 얓은 복사
a=[10]
id(a)
b=a[:]
a.append(11)
a
id(a)
b
id(b)



#return 의 의미
result=[]
def solution(x,n):
    result.append(n)
    return result
def diff_solution(x,n):
    result.append(n)

#이럴땐 굳이...?
def test1(x,n):
    return x

def test2(x,n):
    x.append(n)

answer=test1(result,5)
answer

test2(result,5)
result

id(answer)
id(result)

a=[1,2,3,4]
a.sort(reverse=True)
a
a="001100"
list(a)
def solution(x):
    numlist=list(x)
    re_idx=[i for i in range(len(numlist)) if numlist[i]!=numlist[0]]
    return len(set([x[1]-x[0] for x in enumerate(re_idx)])) if re_idx else 0
    # for i in range(len(numlist)):
    #     if numlist[i]!=numlist[0]:
    #         re_idx.append(i)
    # #특수사항 000 or 001
    # if re_idx==[]:
    #     return 0
    # # if len(re_idx)==1:
    #     return 1
    # n,result=0,0
    # while n<len(re_idx)-1:
    #    if re_idx[n]+1!=re_idx[n+1]:
    #        result+=1
    #     n+=1
    # return result+1
solution('01101110')
list(zip([1,2,3],['가','나','디']))
solution('10110001')

id(a)