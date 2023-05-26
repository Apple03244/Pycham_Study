while True:
    n = int(input("리스트의 크기를 입력하세요: "))
    if n>10:
        print("리스트의 크기를 다시 정하세요")
        continue
    result=[]
    for i in range(n):
        result.append(int(input("리스트의 값을 할당해보세요 :")))
    break
print(f'크기{n}의 리스트 {result}가 할당되었습니다')

import random
[random.randint(1,45) for i in range(6)]
dir(random)
random.ra