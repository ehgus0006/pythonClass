import random

# 2번같은경우 사용자 입력값 5를 누르면 5줄 나오게
lotto = [i for i in range(1,46)]
n = int(input("뽑을 횟수를 정해주세요 : "))

result = []

# lotto 번호 6개를 출력한다, 중복된 값은 나올수없다, 정렬 sort 처리를한다
for i in range(1, n+1):
    random.shuffle(lotto)
    print("로또번호 (%d번줄) : " %i, end=" ")
    for j in range(6): # 6개출력 1번에대해서 다뽑고 새로 shuffle
        print("%2d" %(lotto[j]), end=" ")
    print()
