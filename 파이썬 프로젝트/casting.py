#타입 변환 casting
a=input("첫번째 실수를 입력하시오: ")
b=input("두번째를 입력하시오: ")
l=list(map(lambda x:float(x)//1,[a,b]))

print("정수부분의 합은", sum(l))

a=3.14

#각 자릿수를 입력받은 후 각각의 자릿수 출력해보자~~

a=int(input("정수를 입력하시오"))
for x in list(str(a)):
    print(int(x))

(a//10)//10
a//10
a%10