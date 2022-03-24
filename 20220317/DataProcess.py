s = "python programming"

# 첨자
print(s[2]) # t
print(s[-2]) # n

# 슬라이스
print(s[2:5]) # tho
print(s[3:]) # hon programming
print(s[:4]) # pyth
print(s[2:-2]) # thon programming

# 길이
print(len(s)) # 18

# 빈도수
print(s.count('n')) #2

# 위치 찾기
print(s.find('o')) #4
print(s.rfind('o')) #9
print(s.index('n', 6)) #16

# 특정 문자 포함 조사
print('pro' in s) # True
print('x' not in s) # True

# 왼쪽/오른쪽/양쪽 공백 제거
print(s.lstrip())
print(s.rstrip())
print(s.strip())

# 구분자로 분할
print(s.split()) # ['python', 'programming']
print(s.split("pro")) # ['python', 'gramming']





