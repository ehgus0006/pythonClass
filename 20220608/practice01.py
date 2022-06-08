

# 랜덤수 ( 1~100) 발생
import random


# 게임을 몇번 할지 사용자 입력

b = int(input("게임을 몇판 하시겠습니까? : "))
g = 0
sum = 0

for i in range(b):
    c = 1
    a = random.randint(1, 100)
    g += 1
    print(g, "번째 게임")
    while(True):

        u = int(input("수를 입력하세요 : "))
        if(a==u):
            break
        elif(a>u): # 랜덤 숫자가 더큰 경우
            print("UP")
        else:
            print("Down")
        c += 1

    sum += c
    print(g, "번째 게임을", c, "번만에 맞췄습니다.")


print("평균적으로 %3.1f 번 만에 맞추었습니다" %(sum/g))

