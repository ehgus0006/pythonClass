import random

# randint(begin, end)
# 일정 범위의 정수 난수 범위 설정

# randrange(begin, end)
# end는 범위에서 제외
# for i in range(5):
    # print(random.random())
    # print(random.randint(1, 10)) # 정수형 랜덤(a가 최소, b가 최대) 10도출력이 된다
    # print(random.randrange(1, 10)) # 10전 까지 출력

# shuffle 함수
# 리스트의 요소 무작위로 섞음

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(food)
random.shuffle(food)
print(food)


