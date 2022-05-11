import random


rand = list()

user_numbers = []
lucky_numbers = []

print("1~45까지의 숫자 6개 입력하세요.")

# 추첨 엔트리용 숫자를 고른다
while 0 <= len(user_numbers) < 6:
    input_numbers = input("> ")

    try:
        a = int(input_numbers)
    except:
        print("무효한 값입니다. 다시입력하세요.")
        continue

    if 0 > a or a > 45:
        print("1~45까지의 숫자를 입력하십시오.")
        continue
    elif a in user_numbers:
        print(user_numbers, "이외의 숫자를 입력하십시오.")
        continue
    else:
        user_numbers.append(a)
print("당신이 고른 숫자는", user_numbers, "입니다. \n")

# 당첨 번호를 고른다
print("컴퓨터 추첨을 시작합니다.")

while 0 <= len(lucky_numbers) < 6:
    b = random.randint(1, 45)
    if b not in lucky_numbers:
        lucky_numbers.append(b)
    else:
        continue

print(lucky_numbers , "\n")


# 추첨엔트리용 번호와 당첨 번호를 비교한다.

userset = set(user_numbers)
luckyset = set(lucky_numbers)
winset = userset.intersection(luckyset)

print("당첨된 숫자는", winset)
print("당첨 개수는", len(winset), '개 입니다.')