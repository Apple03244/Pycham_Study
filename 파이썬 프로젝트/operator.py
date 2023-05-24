# and, or, not

a=input("신호등의 색깔 입력 : ")
a.upper()

if a=="G":
    print("진행~")
elif a=="R":
    print("정지!")
else:
    print("주의")


#score

score = int(input("점수를 입력하세요: ")) // 10
result = None
if score >= 9:
    result = "A"
elif score >= 8:
    result = "B"
elif score >= 7:
    result = "C"
elif score >= 6:
    result = "D"
else:
    result = "F"
print('결과는:', result)

#드래그 후에 ctrl+art+l 하면 줄맞춤

#빠르게 해결해볼까
p=int(input())//1000
if p >= 50:
    d = 0.2
elif p >= 10:
    d = 0.1
elif p >= 5:
    d = 0.05
else:
    d = 0
print("입력: ",p)
print("할인금액: ",d*p*1000)

