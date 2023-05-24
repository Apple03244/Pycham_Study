for i in range(10):
    print("@",end="")

#구구단
a,b=int(input("몇단?: ")),int(input("어디까지?: "))
for x in range(b):
    # print(a,"X",b,"=",a*b)
    print(f'{a}X{b}=',a*b)

for x in range(2002,2022+1,4):
    print(x)

n=int(input("자연수 입력 : "))
for x in range(1,n+1):
    if n%x==0:
        print(x,end="\t")