import random

max = int(input("게임횟수 : "))
c = 0 # 정답횟수
count = 0 # 출제 문제
x, y = [], [] # 출제된 문제 저장 목록
flag = 0 # 중복 발생

while (count < max):
    a = random.randint(2, 9) # 단
    b = random.randint(1, 9)
    s = str(a) + " x " + str(b) + " ="
    for i in range(len(x)):
        if(a == x[i] and b == y[i]):
            print("중복 발생: %d X %d " % (a, b))
            flag = 1 # 중복 발생 표시 깃발
            break # for 문 종료
    if flag == 1:
        flag = 0
        continue
    ans = int(input(s))
    x.append(a) # 출제문제 목록에 추가
    y.append(b) # 출제문제 목록에 추가
    if ans == a*b:
        print("정답")
        c += 1
    else:
        print("오답~~ (답:", a*b,")")
    count += 1

print("총 %d 문제중 %d개 정답이었음" % (max, c))
