# 함수

def calcSum(n):
    sum = 0
    for num in range(n+1):
        sum += num
    return sum

print("4 =", calcSum(4))
print("10 =", calcSum(10))

# 인수

def calcrange(begin, end):
    sum = 0
    for num in range(begin, end+1):
        sum += num
    return sum
print("3~7까지의 합 =" , calcrange(3,7))

# 가변 인수
# 고정되지 않은 임의 개수의 인수를 받음
# 인수 목록의 마지막에 와야 함
# ex)

def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum
print(intsum(1, 2, 3)) # 6
print(intsum(5, 7, 9, 11, 13)) #45
print(intsum(8, 9, 6, 2, 9, 7, 5, 8)) #54

# 키워드 인수
# 인수 이름 지정하여 대입 형태로 전달하는 방식
# 앞쪽에 키워드 인수 있으면 뒤쪽에 위치 인수 올 수 없음


