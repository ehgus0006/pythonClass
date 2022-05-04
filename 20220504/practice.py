# a = int(input("몇 단을 출력하시겠습니까? : "))
# for i in range(1, 10):
#     print(a, "X", i, "=", a*i)



# a = int(input("시작단 입력 : "))
# s = ""
# for k in range(a,10):
#     s += " " + str(k) + "단         "
# print(s)
# print("-" * (9-a+1)*12)
# for i in range(1, 10):
#     for j in range(a, 10):
#         print(j, "X", i, "=", j*i, end="\t")
#     print("")


a = [100, 101, 102]
b = [200, 201, 202]

c = a.copy()

# 주소 번지가 공유되어 c=a 일때 c나 a를 수정하면 둘다 값이 변경된다
c[0]=1000
print(a)


