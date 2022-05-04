# 1번
# 배열 1부터 45까지
import random

lotto = [i for i in range(1,46)]

# random 으로 1,45까지 뽑으면서 중복방지를 위해 pop 삭제를 해야한다
for i in range(6):
    random.shuffle(lotto)
    lotto.pop(i)

# lotto 번호 6개를 출력한다, 중복된 값은 나올수없다, 정렬 sort 처리를한다
for j in range(6):
    print(lotto[j], end=" ")








# 3번 같은경우 함수화 def