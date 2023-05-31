#파일 시스템 입출력 라이브러리 open(w,r,a)->
# #open을 했을시 파일이 없으면 자동생성
# f=open("test.txt","w")
#w:덮어쓰기,r:읽기,a:cnrk
# f.close()

f=open("test.txt","w",encoding='UTF=8')
for i in range(10):
    data=f'{i}번째 줄입니다. \n'
    f.write(data)
f.close()


f=open("test.txt","r",encoding='UTF=8')
while True:
    line=f.readline()
    if not line:
        break

 line1.flisne()
f.close()

import os
#os
searchDir=r'D:\Pycham_Study\파이썬 프로젝트'
#파일,디렉토리 목록을 뽑아내는 listdir 함수
dirlist=os.listdir(searchDir)
for dir in dirlist:
    dt=os.path.splitext(dir)
    if dt[1]==".py":
        fullpath=os.path.join(searchDir,dir)
        if os.path.isdir(fullpath):
            print(fullpath,"디랙토리")
        else:
            print(fullpath)

#내가 해줘?
path=r'D:\Pycham_Study'
dirlist=os.listdir(path)
pylist=[]

def search(path):
    result=[]
    for dir in dirlist:
       if os.path.splitext(dir)[1]==".py":
            pylist.appned(os.path.join(path,dir))
       elif os.path.isdir(os.path.join(path,dir)):
           result.append(os.path.join(path,dir))
    return result
