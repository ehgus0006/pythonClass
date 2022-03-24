# 리스트

score = [ 88, 95, 70, 100, 99 ]
sum = 0
for s in score:
    sum += s
print("총점 :", sum)
print("평균 :", sum / len(score))


# 요소 분리 : 범위 지정
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

# 리스트 컴프리헨션
# [수식 for 변수 in 리스트 if 조건]

# nums = [n * 2 for n in range(1, 11)]
# for i in nums:
#     print(i, end= ', ')


# 범위에 리스트 대입하여 여러 요소 한꺼번에 삽입 가능
num = [1, 2, 3, 4]
num[2:2] = [90, 91, 92]
print(num)

num = [1, 2, 3, 4]
num[2] = [90, 91, 92]
print(num)

# 여러 값을 삭제할려면 for문을 돌려야한다
num = [1, 2, 3, 4, 1]
num.remove(1)
print(num)

# 검색
# index : 특정 요소 위치 찾음
# count : 특정 요소값의 개수 조사
# 문자열 출력할때는 +, 숫자 타입은 ,

score = [88, 95, 70, 100, 99, 80, 78, 50]
perfect = score.index(100)
print("만점 받은 학생은 :", perfect ,"번 입니다")
pernum = score.count(100)
print("만점자 수는 ", pernum, "명입니다" )

# 정렬
# sort()와 sorted()의 가장 큰 차이점은 sorted()는 리스트와 문자열 둘 다 적용이 가능하지만
# sort()는 리스트만 가능하다
# 사용법 nums.sort(), sorted(변수)

